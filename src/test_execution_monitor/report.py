import csv
import time
from functools import wraps

from .decorators import test_results


class SkipTest(Exception):
    pass


def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        test_result = {
            "test_name": wrapper.__name__,
            "status": "FAIL",
            "failure_reason": None,
            "execution_time": 0.0,
        }

        print(f"Starting test: {wrapper.__name__}")
        start_time = time.perf_counter()
        try:
            result = func(*args, **kwargs)
            test_result["status"] = "PASS"
            return result
        except SkipTest as error:
            test_result["status"] = "SKIPPED"
            test_result["failure_reason"] = str(error)
            raise
        except Exception as error:
            test_result["status"] = "FAIL"
            test_result["failure_reason"] = str(error)
            raise
        finally:
            end_time = time.perf_counter()
            execution_time = end_time - start_time
            test_result["execution_time"] = execution_time
            test_results.append(test_result)

    return wrapper


def generate_report(test_results: list) -> dict:
    """This is summary overall report"""
    report = {}
    total = len(test_results)
    passed = sum(result["status"] == "PASS" for result in test_results)
    failed = sum(result["status"] == "FAIL" for result in test_results)
    skipped = sum(result["status"] == "SKIPPED" for result in test_results)
    total_execution_time = sum(result["execution_time"] for result in test_results)
    executed = total - skipped
    pass_rate = (passed / executed) * 100 if executed > 0 else 0
    report["total"] = total
    report["passed"] = passed
    report["failed"] = failed
    report["skipped"] = skipped
    report["pass_rate"] = round(pass_rate, 2)
    report["total_execution_time"] = total_execution_time
    report["avarge_execution_time"] = (
        total_execution_time / executed if executed > 0 else 0
    )
    return report


def export_results_to_csv(test_results: list, file_path: str) -> None:
    fields = [
        "test_name",
        "status",
        "failure_reason",
        "execution_time",
    ]

    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(test_results)
