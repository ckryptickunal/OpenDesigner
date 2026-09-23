// OpenDesigner report receiver: a reference Cloudflare Worker (BRIEF requirement 19). Nothing is deployed;
// hosting is the maintainers' decision. See README.md and docs/PRIVACY.md.
//
// It accepts only anonymous reports that pass report.schema.json and are at most 16 KB. It stores the report and
// the ISO week it arrived. It never stores the IP address, the user agent, any other header, or the exact time.
import schema from "../../skills/opendesigner/references/report.schema.json" with { type: "json" };
import { validate } from "./validate.js";

const MAX_BYTES = 16384;  // journey.py MAX_REPORT_BYTES; a full detailed run of all 192 questions is about 14 KB
const KEEP_WEEKS = 52;    // raw reports are deleted after 12 months

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname !== "/v1/reports") return reply(404, "not found");
    if (request.method !== "POST") return reply(405, "use POST");
    // Flood protection. The address is only a counter key that Cloudflare holds for one minute. It is never stored.
    const { success } = await env.RATE_LIMITER.limit({ key: request.headers.get("CF-Connecting-IP") || "unknown" });
    if (!success) return reply(429, "too many reports, try again later");
    if (Number(request.headers.get("Content-Length") || 0) > MAX_BYTES) return reply(413, "report too large");
    const body = await request.arrayBuffer();
    if (body.byteLength > MAX_BYTES) return reply(413, "report too large");
    let report;
    try {
      report = JSON.parse(new TextDecoder().decode(body));
    } catch {
      return reply(400, "not JSON");
    }
    const errors = validate(report, schema);
    if (errors.length) return reply(400, "report does not match the schema", errors.slice(0, 5));
    await env.DB.prepare("INSERT OR IGNORE INTO reports (id, received_week, payload) VALUES (?1, ?2, ?3)")
      .bind(report.report_id, isoWeek(new Date()), JSON.stringify(report))
      .run();
    return reply(202, "thank you");
  },

  // Runs on the cron in wrangler.toml: delete raw reports older than 12 months. Published aggregates stay.
  async scheduled(controller, env) {
    const cutoff = isoWeek(new Date(Date.now() - KEEP_WEEKS * 7 * 86400000));
    await env.DB.prepare("DELETE FROM reports WHERE received_week < ?1").bind(cutoff).run();
  },
};

function reply(status, message, details) {
  return new Response(JSON.stringify(details ? { message, details } : { message }),
    { status, headers: { "Content-Type": "application/json" } });
}

// ISO 8601 week, such as 2026-W39 (the same form journey.py sends). Sorts correctly as text.
export function isoWeek(date) {
  const d = new Date(Date.UTC(date.getUTCFullYear(), date.getUTCMonth(), date.getUTCDate()));
  d.setUTCDate(d.getUTCDate() + 4 - (d.getUTCDay() || 7));
  const week = Math.ceil(((d - Date.UTC(d.getUTCFullYear(), 0, 1)) / 86400000 + 1) / 7);
  return `${d.getUTCFullYear()}-W${String(week).padStart(2, "0")}`;
}
