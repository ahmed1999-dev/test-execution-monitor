
from test_execution_monitor import log_execution, SkipTest, test_results
import pytest


@pytest.fixture(autouse=True)
def prepare_test_data():
    test_results.clear()


def test_successful_function_is_recorded():
    @log_execution
    def sample_test():
        return "success"

    result = sample_test()

    assert result == "success"
    assert len(test_results) == 1
    assert test_results[0]["test_name"] == "sample_test"
    assert test_results[0]["status"] == "PASS"
    assert test_results[0]["failure_reason"] is None
    assert test_results[0]["execution_time"] >= 0


def test_failed_function_is_recorded_and_reraised():
    @log_execution
    def sample_test():
        raise ValueError("This test failed for some reasons")

    with pytest.raises(
        ValueError, match="This test failed for some reasons"
    ):
        sample_test()

    assert len(test_results) == 1
    assert test_results[0]["status"] == "FAIL"
    assert (
        test_results[0]["failure_reason"]
        == "This test failed for some reasons"
    )
    assert test_results[0]["execution_time"] >= 0


def test_skipped_function_is_recorded_and_reraised():
    @log_execution
    def sample_test():
        raise SkipTest("Feature unavailable")

    with pytest.raises(SkipTest, match="Feature unavailable"):
        sample_test()

    assert len(test_results) == 1
    assert test_results[0]["status"] == "SKIPPED"
    assert test_results[0]["failure_reason"] == "Feature unavailable"
    assert test_results[0]["execution_time"] >= 0
