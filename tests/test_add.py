from src import calculator as calc
import unittest

class Test_AddFunctionality(unittest.TestCase):
    calculator = calc.Calculator()
    def test_add_simple(self):
        self.assertEqual(self.calculator.add(1,1), 2)
