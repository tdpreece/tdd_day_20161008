from unittest import TestCase
from parameterizedtestcase import ParameterizedTestMixin

from src.calculator import FibonacciCalculator


class TestFibonacciCalculator(ParameterizedTestMixin, TestCase):
    @ParameterizedTestMixin.parameterize(
        ("input", "expected"),
        [
            (0, 0),
            (1, 1),
        ]
    )
    def test_first_two_numbers_are_same_as_index(self, index, expected):
        self.assertEqual(expected, self.calculate_fibonacci_number_at_index(index))

    @ParameterizedTestMixin.parameterize(
        ("input", "expected"),
        [
            (2, 1),
            (3, 2),
            (5, 5),
        ]
    )
    def test_number_is_index_minus_one(self, index, expected):
        self.assertEqual(expected, self.calculate_fibonacci_number_at_index(index))

    @staticmethod
    def calculate_fibonacci_number_at_index(index):
        return FibonacciCalculator().calculate(index)
