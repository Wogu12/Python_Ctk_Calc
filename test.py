import unittest

from main import CalcWindow


class TestCalc(unittest.TestCase):
    calc = CalcWindow()

    def test_eval_positive(self):
        eq = "23+15"
        self.calc.clear_input()
        self.calc._pressed_buttons.append(eq)
        self.calc.evaluate_expression()
        result = float("".join(self.calc._pressed_buttons))

        self.assertEqual(result, eval(eq), "not equal")

    def test_power(self):
        eq = "12"
        self.calc.clear_input()
        self.calc._pressed_buttons.append(eq)
        self.calc.power_btn()

        result = float("".join(self.calc._pressed_buttons))

        self.assertEqual(result, 144, "not equal")

    def test_sqr(self):
        eq = "-4"
        self.calc.clear_input()
        self.calc._pressed_buttons.append(eq)
        self.calc.sqrt_btn()

        result = float("".join(self.calc._pressed_buttons))

        self.assertEqual(result, int(eq), "not equal")


if __name__ == "__main__":
    unittest.main()
