import unittest
import math as m
import random as r

from main import CalcWindow


class TestCalc(unittest.TestCase):
    calc = CalcWindow()

    def test_power(self):
        num = r.uniform(-9999, 9999)
        eq = str(num)
        self.calc.clear_input()
        self.calc._pressed_buttons.append(eq)
        self.calc.power_btn()

        result = float("".join(self.calc._pressed_buttons))

        num_pwr = round(num**2, 10)
        self.assertEqual(result, num_pwr, "not equal")
        print("Test passed: test_power")

    def test_sqr(self):
        num = r.uniform(1, 9999)
        eq = str(num)
        self.calc.clear_input()
        self.calc._pressed_buttons.append(eq)
        self.calc.sqrt_btn()

        result = float("".join(self.calc._pressed_buttons))

        num_sqrt = round(m.sqrt(num), 10)
        self.assertEqual(result, num_sqrt, "not equal")
        print("Test passed: test_sqr")

    def test_rand_positive(self):
        a = r.uniform(1, 9999)
        b = r.uniform(1, 9999)
        signs = ["+", "-", "*", "/"]

        eq_sign = r.choice(signs)
        eq = f"{a}{eq_sign}{b}"

        self.calc.clear_input()
        self.calc._pressed_buttons.append(eq)
        self.calc.evaluate_expression()
        result = float("".join(self.calc._pressed_buttons))

        self.assertEqual(result, round(eval(eq), 10), "not equal")
        print("Test passed: test_rand_positive")

    def test_rand_all(self):
        a = r.uniform(-9999, 9999)
        b = r.uniform(-9999, 9999)
        signs = ["+", "-", "*", "/"]

        eq_sign = r.choice(signs)

        eq = f"{a}{eq_sign}{b}"

        self.calc.clear_input()
        self.calc._pressed_buttons.append(eq)
        self.calc.evaluate_expression()
        result = float("".join(self.calc._pressed_buttons))

        self.assertEqual(result, round(eval(eq), 10), "not equal")
        print("Test passed: test_rand_all")

    def test_bad_input(self):
        random_string = "test my func"
        self.calc.clear_input()
        self.calc._pressed_buttons.append(random_string)

        with self.assertRaises(SyntaxError):
            self.calc.evaluate_expression()
        print("Test passed: test_bad_input")


if __name__ == "__main__":
    unittest.main()
