from unittest import TestCase

from parameterizedtestcase import ParameterizedTestMixin


class TestCheckout(ParameterizedTestMixin, TestCase):
    def test_no_items_return_zero(self):
        self.assertEqual(0, total([]))

    @ParameterizedTestMixin.parameterize(
        ('items', 'expected_total'),
        [
            ([{'price': 5, 'quantity': 1}], 5),
            ([{'price': 5, 'quantity': 2}], 10),
            ([{'price': 1, 'quantity': 1}, {'price': 1, 'quantity': 1}], 2),
        ]
    )
    def test_total_is_price_times_quanity(self, items, expected_total):
        self.assertEqual(expected_total, total(items))

def total(items):
    return sum(item['price'] * item['quantity'] for item in items)