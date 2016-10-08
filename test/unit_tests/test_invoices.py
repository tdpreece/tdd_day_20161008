from unittest import TestCase
from mock import MagicMock
from parameterizedtestcase import ParameterizedTestMixin

from src.order import Order


class TestInvoice(ParameterizedTestMixin, TestCase):
    @ParameterizedTestMixin.parameterize(
        ("input", "expected"),
        [
            ([{'product': 'x', 'quantity': 1, 'price': 1}], 1),
            ([{'product': 'x', 'quantity': 2, 'price': 1}], 2),
        ]
    )
    def test_check_dvd_instock_for_one_dvd(self, items, total):
        is_in_warehouse = MagicMock(return_value=True)
        imdbRating = MagicMock(return_value=6)
        self.assertEqual(total, Order(items, is_in_warehouse, imdbRating).total())
