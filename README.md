# swe-testing-assignment
# Quick-Calc (SWE Testing Assignment)

Quick-Calc is a small calculator application that supports addition, subtraction, multiplication, division (with graceful division-by-zero handling), and a Clear (C) operation. The main focus of this project is clean, testable code and a multi-layer testing strategy (unit + integration) managed with Git and GitHub.

## Features
- Addition, subtraction, multiplication, division
- Division by zero handled gracefully (shows `Error` at the app layer)
- Clear operation resets state to `0`
- Unit tests for calculation logic + integration tests for user flows

## Tech Stack
- Python 3.12
- Testing: `pytest`

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/Ekomote/swe-testing-assignment.git
   cd swe-testing-assignment