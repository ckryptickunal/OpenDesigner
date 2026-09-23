-- D1 table for the report receiver. One row per report; nothing about the sender.
CREATE TABLE IF NOT EXISTS reports (
  id TEXT PRIMARY KEY,          -- the report's random id, new for every report
  received_week TEXT NOT NULL,  -- ISO week it arrived, such as 2026-W39; no day or time
  payload TEXT NOT NULL         -- the validated report JSON, nothing else
);
CREATE INDEX IF NOT EXISTS reports_by_week ON reports (received_week);
