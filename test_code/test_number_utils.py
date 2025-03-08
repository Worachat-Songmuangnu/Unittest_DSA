import unittest
from production_code.number_utils import is_prime_list

class TestIsPrimeList(unittest.TestCase):
    def test_1_is_not_prime(self):
        self.assertFalse(is_prime_list([1]))

    def test_prime_numbers_2_3_5_7_11_should_return_true(self):
        self.assertTrue(is_prime_list([2, 3, 5, 7, 11]))

    def test_composites_4_6_8_9_10_should_return_false(self):
        self.assertFalse(is_prime_list([4, 6, 8, 9, 10]))

    def test_mixed_2_3_4_5_6_should_return_false(self):
        self.assertFalse(is_prime_list([2, 3, 4, 5, 6]))

    def test_empty_list_should_return_true(self):
        self.assertTrue(is_prime_list([]))
