# Test Execution Monitor

A Python-based tool for monitoring test execution, tracking test results, measuring execution time, and generating reports.

## Overview

Test Execution Monitor provides a simple way to track automated test execution results. It uses Python decorators to capture execution details and generates summary reports to help analyze test outcomes.

The project demonstrates Python automation concepts, exception handling, decorators, reporting, CSV export, and automated testing with pytest.

## Features

- **Test execution tracking:** Records each test's execution status.
- **Status classification:** Tracks passed, failed, and skipped tests.
- **Execution timing:** Measures individual test execution time.
- **Exception handling:** Captures failure reasons while preserving exception propagation.
- **Execution reports:** Generates summary statistics and pass rates.
- **CSV export:** Exports test execution results to CSV files.
- **Automated testing:** Includes pytest tests to validate the functionality.
- **Code quality:** Uses Ruff for linting and formatting.
- **CI/CD:** Uses GitHub Actions to automate quality checks and test execution.

## Project Structure

```text
test-execution-monitor/
├── .github/
│   └── workflows/
│       └── tests.yml
├── examples/
│   └── demo.py
├── src/
│   └── test_execution_monitor/
│       ├── __init__.py
│       ├── decorators.py
│       └── report.py
├── tests/
│   ├── test_decorators.py
│   └── test_report.py
├── .gitignore
├── pyproject.toml
├── README.md
└── uv.lock
```

## Requirements

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)

## Installation

Clone the repository:

```bash
git clone https://github.com/ahmed1999-dev/test-execution-monitor.git
cd test-execution-monitor
```

Install project dependencies:

```bash
uv sync
```

## Usage

Run the demonstration:

```bash
uv run python examples/demo.py
```

The demonstration executes sample tests and displays an execution summary.

## Running Tests

Run the automated test suite:

```bash
uv run pytest
```

## Code Quality

Check code using Ruff:

```bash
uv run ruff check .
```

Verify formatting:

```bash
uv run ruff format --check .
```

## Continuous Integration

GitHub Actions automatically runs the project's quality checks and pytest suite when changes are pushed to the main branch or a pull request is created.

## Technologies

- Python
- pytest
- Ruff
- uv
- GitHub Actions
- CSV

## Future Improvements

- HTML execution reports
- Logging integration
- Test execution history
- Filtering and grouping results
- Parallel test execution support

## Author

Ahmed Hatem