import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")

# Ground truth for /app/access.log, computed independently of the agent's code:
# 6 non-blank request lines; 3 distinct client IPs (192.168.0.1, 192.168.0.2,
# 10.0.0.5); /index.html requested 3 times, more than any other path.
EXPECTED_TOTAL_REQUESTS = 6
EXPECTED_UNIQUE_IPS = 3
EXPECTED_TOP_PATH = "/index.html"


def _load_report():
    assert REPORT_PATH.exists(), "no report.json found at /app/report.json"
    with open(REPORT_PATH) as f:
        return json.load(f)


def test_report_exists_and_is_valid_json():
    """Success criterion 1: /app/report.json exists and contains valid JSON."""
    report = _load_report()
    assert isinstance(report, dict)


def test_total_requests():
    """Success criterion 2: total_requests matches the true request count."""
    report = _load_report()
    assert report.get("total_requests") == EXPECTED_TOTAL_REQUESTS, (
        f"expected total_requests={EXPECTED_TOTAL_REQUESTS}, "
        f"got {report.get('total_requests')!r}"
    )


def test_unique_ips():
    """Success criterion 3: unique_ips matches the true distinct-IP count."""
    report = _load_report()
    assert report.get("unique_ips") == EXPECTED_UNIQUE_IPS, (
        f"expected unique_ips={EXPECTED_UNIQUE_IPS}, got {report.get('unique_ips')!r}"
    )


def test_top_path():
    """Success criterion 4: top_path matches the single most-requested path."""
    report = _load_report()
    assert report.get("top_path") == EXPECTED_TOP_PATH, (
        f"expected top_path={EXPECTED_TOP_PATH!r}, got {report.get('top_path')!r}"
    )
