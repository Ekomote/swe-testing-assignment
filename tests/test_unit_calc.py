import pytest
from quick_calc.calc import add, subtract, multiply, divide, CalculatorError


def test_addition_basic():
    assert add(5, 3) == 8


def test_subtraction_basic():
    assert subtract(10, 4) == 6


def test_multiplication_basic():
    assert multiply(6, 7) == 42


def test_division_basic():
    assert divide(20, 4) == 5


def test_division_by_zero_raises():
    with pytest.raises(CalculatorError):
        divide(10, 0)


def test_negative_numbers():
    assert add(-5, -3) == -8
    assert subtract(-5, -3) == -2


def test_decimal_numbers():
    assert add(0.1, 0.2) == pytest.approx(0.3)


def test_very_large_numbers():
    big = 10**18
    assert multiply(big, 2) == 2 * big