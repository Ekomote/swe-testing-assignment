# Testing Strategy for Quick-Calc

## What Was Tested
### Unit Tests (Logic Layer)
- `add`, `subtract`, `multiply`, `divide`
- Edge cases:
  - Division by zero (raises `CalculatorError` at the logic layer)
  - Negative numbers
  - Decimal numbers (using `approx` for floating-point)
  - Very large numbers

### Integration Tests (Input Layer + Logic)
- Full user interaction flow (e.g., `5 + 3 = 8`)
- Clear resets state and display to `0`
- Division by zero handled gracefully at the app layer (display becomes `Error`)

## What Was Not Tested (And Why)
- UI rendering was not tested because the assignment focus is testing strategy and correctness rather than UI.
- Non-functional tests such as performance, security, accessibility, and usability were intentionally not included due to the small scope of the application.
- Output formatting rules (e.g., removing trailing `.0`) were not enforced; the project prioritizes correctness and coverage over display formatting.

## Relation to Lecture 3 Concepts

### 1) Testing Pyramid
This project follows the Testing Pyramid:
- Many unit tests validate small pieces (calculation functions) quickly and reliably.
- Fewer integration tests validate that the input-layer model correctly interacts with the calculation logic.
This keeps the suite fast while still providing confidence that components work together.

### 2) Black-box vs White-box Testing
- Unit tests are closer to white-box testing because they target specific functions and include edge cases derived from how the logic behaves (e.g., raising on division by zero).
- Integration tests are closer to black-box testing because they simulate user behavior (button presses) and assert visible outcomes (the display), without calling the math functions directly.

### 3) Functional vs Non-Functional Testing
- The suite focuses on functional testing: correct results for operations and correct behavior for Clear and division-by-zero handling.
- Non-functional testing is intentionally out of scope for this small educational application.

### 4) Regression Testing
The test suite can be run after any future change to catch regressions. If a change breaks an operation or user flow, running `python -m pytest -q` will fail and highlight the issue early.

## Test Results Summary

| Test Name                              | Type        | Status |
|----------------------------------------|-------------|--------|
| test_addition_basic                     | Unit        | Pass   |
| test_subtraction_basic                  | Unit        | Pass   |
| test_multiplication_basic               | Unit        | Pass   |
| test_division_basic                     | Unit        | Pass   |
| test_division_by_zero_raises            | Unit        | Pass   |
| test_negative_numbers                   | Unit        | Pass   |
| test_decimal_numbers                    | Unit        | Pass   |
| test_very_large_numbers                 | Unit        | Pass   |
| test_full_user_interaction_addition     | Integration | Pass   |
| test_clear_resets_after_calculation     | Integration | Pass   |
| test_division_by_zero_is_graceful       | Integration | Pass   |