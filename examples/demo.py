import time

from test_execution_monitor import (
    SkipTest,
    generate_report,
    log_execution,
    test_results,
)


@log_execution
def test_login():
    """Test login."""
    time.sleep(1)
    print("Testing login...")


@log_execution
def test_logout():
    """Test logout."""
    time.sleep(0.5)
    print("Testing logout...")


@log_execution
def test_payment():
    """Test payment."""
    time.sleep(2)
    raise ValueError("Payment failed")


@log_execution
def test_skipped():
    """Test skipped execution."""
    raise SkipTest("Profile feature is not available")


if __name__ == "__main__":
    for test in [test_login, test_logout, test_payment, test_skipped]:
        try:
            test()
        except (SkipTest, ValueError) as error:
            print(f"Test execution result: {error}")

        print(generate_report(test_results))
