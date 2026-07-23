log-report
Terminal-Bench 2 (Harbor) task: parse an Apache-style access log and write a JSON summary (total_requests, unique_ips, top_path) to /app/report.json.

Run it with Harbor:

harbor run -p . -a oracle     # reference solution -> reward 1
harbor run -p . --agent nop   # no-op agent -> reward 0
See instruction.md for the full task spec and tests/test_outputs.py for the verifier.
