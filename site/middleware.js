// Markdown for agents (opendesigner.dev): a request whose Accept header asks for text/markdown gets the page's Markdown
// copy, which every page already has at <path>index.md. Browsers and search engines keep getting HTML. Vercel Routing
// Middleware with plain Web APIs and no packages. Vercel serves existing files before vercel.json rewrites, so a
// rewrite alone can't do this.
export const config = { matcher: ["/", "/:path*/"] };

export default function middleware(request) {
  const accept = request.headers.get("accept") || "";
  if (!/\btext\/markdown\b/i.test(accept)) return; // carry on to the HTML page
  const url = new URL(request.url);
  if (!url.pathname.endsWith("/")) return;
  url.pathname += "index.md";
  return new Response(null, { headers: { "x-middleware-rewrite": url.toString(), vary: "Accept" } });
}
