# from controllers.calculator import Calculator
from src.calculator import Calculator
import re
import unittest

class Test_CalcFunctionality(unittest.TestCase):
    calculator = Calculator()
    def test_add_simple(self):
        self.assertEqual(self.calculator.add(1,1), 2)

    def test_fails_if_input_is_invalid(self):
        result = self.calculator.evalute(dict(input="sdf+t"))
        regex = r".*m confused.*"
        match = re.match(regex, result['errorMessage'])
        self.assertNotEqual(match, None)

    def test_fails_if_input_is_attempting_something_bad(self):
        result = self.calculator.evalute(dict(input="sudo reboot"))
        regex = r".*m confused.*"
        match = re.match(regex, result['errorMessage'])
        self.assertNotEqual(match, None)

    def test_supports_evaluating_single_digit_number(self):
        result = self.calculator.evalute(dict(input="5"))
        self.assertEqual(result['output'], 5)

    def test_supports_evaluating_many_digit_number(self):
        result = self.calculator.evalute(dict(input="25"))
        self.assertEqual(result['output'], 25)

    def test_supports_evaluating_integer_sums(self):
        result = self.calculator.evalute(dict(input="2+5"))
        self.assertEqual(result['output'], 7)

    def test_supports_evaluating_integer_subtractions(self):
        result = self.calculator.evalute(dict(input="2-5"))
        self.assertEqual(result['output'], -3)

    def test_supports_evaluating_mixed_operations(self):
        result = self.calculator.evalute(dict(input="2-5+9*2"))
        self.assertEqual(result['output'], 15)

    def test_warns_user_they_typed_something_weird(self):
        result = self.calculator.evalute(dict(input="2-5+9*/2"))
        regex = r".*learned how to.*"
        match = re.match(regex, result['errorMessage'])
        self.assertNotEqual(match, None)