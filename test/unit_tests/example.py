from unittest import TestCase

from mock import MagicMock
from parameterizedtestcase import ParameterizedTestMixin


class TestSomething(ParameterizedTestMixin, TestCase):
    @ParameterizedTestMixin.parameterize(
        ("input", "expected_output"),
        [
            (1, 1),
        ]
    )
    def test(self, input, expected_output):
        self.assertEqual(input, expected_output)

    def test_a_mock(self):
        my_mock = MagicMock(return_value=1)
        self.assertEqual(1, my_mock())
