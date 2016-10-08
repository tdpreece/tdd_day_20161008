from unittest import TestCase


from src.title import Title
from src.library import Library
from src.donation_fixture import DonationFixture

class TestDonationFixture(TestCase):
    def libraryContains(self):
        donationFixture = DonationFixuture()
        self.assertTrue(donationFixture.libraryContains())

    def libraryContains(self):
        donationFixture = DonationFixuture()
        self.assertEqual(1, donationFixture.copyCount())

    def libraryContains(self):
        donationFixture = DonationFixuture()
        self.assertEqual(10,donationFixture.rewardPoint())

    def libraryContains(self):
        donationFixture = DonationFixuture()
        self.assertEqual("available new title",donationFixture.emailSubject())

    def libraryContains(self):
        donationFixture = DonationFixuture()
        self.assertEqual("", donationFixture.emailBody())

    def libraryContains(self):
        donationFixture = DonationFixuture()
        self.assertEqual("",donationFixture.recipient())


class TestLibrary(TestCase):
    def test_library_contains(self):
        title = Title()
        library = Library()
        library.donate(title)
        self.assertTrue(library.contains(title))

    def test_copy_count(self):
        title = Title()
        library = Library()
        library.donate(title)
        self.assertEqual(1, library.copy_count(title))
