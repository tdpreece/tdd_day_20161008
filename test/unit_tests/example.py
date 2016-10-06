from unittest import TestCase
from parameterizedtestcase import ParameterizedTestMixin


class TestSomething(ParameterizedTestMixin, TestCase):
    @ParameterizedTestMixin.parameterize(
        ("input", "expected_output"),
        [
            (1, 2),
        ]
    )
    def test(self, input, expected_output):
        self.assertEqual(input, expected_output)
