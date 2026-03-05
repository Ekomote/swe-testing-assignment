from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from quick_calc.calc import add, subtract, multiply, divide, CalculatorError


@dataclass
class QuickCalcApp:
    """Simple input-layer model that simulates button presses."""

    display: str = "0"
    _current: str = ""
    _pending_op: Optional[str] = None
    _left: Optional[float] = None

    def press_digit(self, digit: str) -> None:
        if digit not in "0123456789":
            raise ValueError("digit must be 0-9")

        if self._current == "0":
            self._current = digit
        else:
            self._current += digit

        self.display = self._current or "0"

    def press_decimal(self) -> None:
        if self._current == "":
            self._current = "0."
        elif "." not in self._current:
            self._current += "."
        self.display = self._current

    def press_clear(self) -> None:
        self.display = "0"
        self._current = ""
        self._pending_op = None
        self._left = None

    def press_op(self, op: str) -> None:
        if op not in {"+", "-", "*", "/"}:
            raise ValueError("op must be one of + - * /")

        if self._left is not None and self._current != "" and self._pending_op is not None:
            self.press_equals()

        if self._left is None:
            self._left = float(self._current) if self._current != "" else float(self.display)

        self._pending_op = op
        self._current = ""

    def press_equals(self) -> None:
        if self._pending_op is None or self._left is None:
            self.display = self._current or self.display
            return

        right = float(self._current) if self._current != "" else 0.0

        try:
            if self._pending_op == "+":
                result = add(self._left, right)
            elif self._pending_op == "-":
                result = subtract(self._left, right)
            elif self._pending_op == "*":
                result = multiply(self._left, right)
            else:
                result = divide(self._left, right)

            self.display = str(result)
            self._left = result
            self._current = ""
            self._pending_op = None

        except CalculatorError:
            self.display = "Error"
            self._current = ""
            self._pending_op = None
            self._left = None