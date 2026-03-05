# Quick-Calc (SWE Testing Assignment)

Quick-Calc is a small calculator application that supports addition, subtraction, multiplication, division (with graceful division-by-zero handling), and a Clear (C) operation. The main focus of this project is clean, testable code and a multi-layer testing strategy (unit + integration) managed with Git and GitHub.

## Features
- Addition, subtraction, multiplication, division
- Division by zero handled gracefully (shows `Error` at the app layer)
- Clear operation resets state and display to `0`
- Unit tests for calculation logic + integration tests for user flows

## Setup Instructions

1. Clone the repository:
   git clone https://github.com/Ekomote/swe-testing-assignment.git
   cd swe-testing-assignment

2. Install dependencies:
   python -m pip install -r requirements.txt

## How to Run Tests

Run the full test suite with:
python -m pytest -q

## Testing Framework Research (pytest vs unittest)

`unittest` is Python’s built-in testing framework and follows an xUnit-style structure using classes, setup/teardown methods, and specific assertion methods. Its advantages are that it requires no additional dependencies, is stable, and is widely supported. However, it can be verbose for small projects: simple tests often require extra boilerplate (test classes, method naming conventions, and more structured assertions), which can reduce readability.

`pytest` is a popular third-party framework known for its clean syntax and powerful features such as fixtures and parametrization. It allows tests to be written as plain functions and uses Python’s native `assert` statements, making tests easier to read and write. It also has a large plugin ecosystem for reporting, coverage, and CI integrations. The main downside is the extra dependency and the need to keep fixture usage consistent so the suite stays understandable as it grows.

Choice: This project uses `pytest` because it keeps tests concise and readable with minimal boilerplate, while still supporting edge-case coverage and integration-style testing as the project expands.