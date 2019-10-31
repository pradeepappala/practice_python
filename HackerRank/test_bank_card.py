import unittest
import bank_card
from unittest import mock
from unittest.mock import patch, PropertyMock


class TestIsCardIdValid(unittest.TestCase):
    def test_card_id(self):
        self.assertFalse(bank_card.is_valid('123456789'))
        self.assertFalse(bank_card.is_valid('1234567890123456'))
        self.assertTrue(bank_card.is_valid('4234567890123456'))
        self.assertTrue(bank_card.is_valid('4234-5678-9012-3456'))
        self.assertFalse(bank_card.is_valid('42345-5678-9012-3456'))
        self.assertFalse(bank_card.is_valid('4234-25678-9012-3456'))
        self.assertTrue(bank_card.is_valid('4234-5678-9992-3456'))
        self.assertFalse(bank_card.is_valid('4234-5678-99922-3456'))
        self.assertFalse(bank_card.is_valid('4234-5678-9992-23456'))
        self.assertFalse(bank_card.is_valid('4234-5679-9992-3456'))
        self.assertFalse(bank_card.is_valid('4555-5678-9992-3456'))
        self.assertFalse(bank_card.is_valid('4234-5678-9999-3456'))
        self.assertFalse(bank_card.is_valid('4234-5678-9999-9999'))


if __name__ == '__main__':
    unittest.main()