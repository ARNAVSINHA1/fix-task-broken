import json
from pathlib import Path

REPORT = Path("/app/report.json")


def load_report():
    assert REPORT.exists(), "report.json was not created"

    with REPORT.open() as f:
        return json.load(f)


def test_output_file_exists():
    """Success Criterion 1: report.json must be created."""
    assert REPORT.exists(), "report.json not found"


def test_report_schema():
    """Success Criterion 2: report.json must contain the required fields."""
    report = load_report()

    assert "total_requests" in report
    assert "unique_ips" in report
    assert "top_path" in report


def test_report_values():
    """Success Criterion 3: report values must be correct."""
    report = load_report()

    assert report["total_requests"] == 6
    assert report["unique_ips"] == 3
    assert report["top_path"] == "/index.html"
