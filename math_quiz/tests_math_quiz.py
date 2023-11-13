import unittest
from math_quiz import integer, operator, calculate_answer

class TestMathQuizFunctions(unittest.TestCase):

    def test_integer(self):
        # Test the integer function to ensure it generates values within the specified range
        min_value = 1
        max_value = 10
        result = integer(min_value, max_value)
        self.assertTrue(min_value <= result <= max_value)

    def test_operator(self):
        # Test the operator function to ensure it returns one of the valid operators
        valid_operators = {'+', '-', '*'}
        result = operator()
        self.assertIn(result, valid_operators)

    def test_calculate_answer(self):
        # Test the calculate_answer function with known values
        a1 = 5
        a2 = 3
        op = '+'
        result = calculate_answer(a1, a2, op)
        self.assertEqual(result, a1 + a2)

        a1 = 8
        a2 = 4
        op = '-'
        result = calculate_answer(a1, a2, op)
        self.assertEqual(result, a1 - a2)

        a1 = 2
        a2 = 6
        op = '*'
        result = calculate_answer(a1, a2, op)
        self.assertEqual(result, a1 * a2)

if __name__ == '__main__':
    unittest.main()
