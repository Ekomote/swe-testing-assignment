from quick_calc.app import QuickCalcApp


def test_full_user_interaction_addition():
    app = QuickCalcApp()
    app.press_digit("5")
    app.press_op("+")
    app.press_digit("3")
    app.press_equals()
    assert app.display in {"8.0", "8"}


def test_clear_resets_after_calculation():
    app = QuickCalcApp()
    app.press_digit("9")
    app.press_op("*")
    app.press_digit("9")
    app.press_equals()
    assert app.display in {"81.0", "81"}

    app.press_clear()
    assert app.display == "0"


def test_division_by_zero_is_graceful():
    app = QuickCalcApp()
    app.press_digit("7")
    app.press_op("/")
    app.press_digit("0")
    app.press_equals()
    assert app.display == "Error"