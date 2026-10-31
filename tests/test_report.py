import csv

from test_execution_monitor import *


def test_report_counts_statuses():
    results = [
        {"status": "PASS", "execution_time": 1.0},
        {"status": "FAIL", "execution_time": 2.0},
        {"status": "SKIPPED", "execution_time": 0.1},
    ]

    report = generate_report(results)

    assert report["total"] == 3
    assert report["passed"] == 1
    assert report["failed"] == 1
    assert report["skipped"] == 1
    assert report["pass_rate"] == 50.0


def test_report_with_empty_results():
    report = generate_report([])

    assert report["total"] == 0
    assert report["pass_rate"] == 0
    assert report["avarge_execution_time"] == 0


def test_report_when_all_tests_are_skipped():
    results = [
        {"status": "SKIPPED", "execution_time": 1.0},
        {"status": "SKIPPED", "execution_time": 1.0},
        {"status": "SKIPPED", "execution_time": 0.1},
    ]
    report = generate_report(results)

    assert report["total"] == 3
    assert report["passed"] == 0
    assert report["failed"] == 0
    assert report["skipped"] == 3
    assert report["pass_rate"] == 0.0
    assert report["total_execution_time"] == 2.1
    assert report["avarge_execution_time"] == 0


def test_export_results_to_csv(tmp_path):
    results = [
        {
            "test_name": "test_login",
            "status": "PASS",
            "failure_reason": None,
            "execution_time": 1.02,
        },
        {
            "test_name": "test_payment",
            "status": "FAIL",
            "failure_reason": "Payment failed",
            "execution_time": 2.01,
        },
    ]

    file_path = tmp_path / "results.csv"

    export_results_to_csv(results, file_path)
    assert file_path.exists()

    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    assert len(rows) == 2
    assert rows[0]["test_name"] == "test_login"
    assert rows[0]["status"] == "PASS"
    assert rows[1]["test_name"] == "test_payment"
    assert rows[1]["status"] == "FAIL"
    assert rows[1]["failure_reason"] == "Payment failed"
