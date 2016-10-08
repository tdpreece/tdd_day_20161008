from unittest import TestCase


class TestCheckout(TestCase):
    def test_no_items_return_zero(self):
        self.assertEqual(0, total())


def total():
    return 0