There is an Apache-style access log at /app/access.log. Parse it and write a JSON summary report to /app/report.json (create the file if it doesn't exist; overwrite it if it does).

The report must be a single JSON object with exactly these keys:

"total_requests" — an integer count of all non-blank lines in /app/access.log.
"unique_ips" — an integer count of distinct client IP addresses (the first whitespace-separated field of each line).
"top_path" — a string with the request path (e.g. "/index.html") that appears most often across all requests, taken from the quoted request line (e.g. "GET /index.html HTTP/1.1").
Success criteria:

/app/report.json exists and contains valid JSON.
"total_requests" matches the true number of requests in the log.
"unique_ips" matches the true number of distinct client IPs in the log.
"top_path" matches the single most-requested path in the log.
