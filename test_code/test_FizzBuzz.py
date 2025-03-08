import unittest
from production_code.FizzBuzz import FizzBuzz

class TestFizzBuzz(unittest.TestCase):

    def test_returns_fizz_for_multiples_of_3(self):
        result = FizzBuzz(6)
        self.assertEqual(result[2], "Fizz") 
        self.assertEqual(result[5], "Fizz") 

    def test_returns_buzz_for_multiples_of_5(self):
        result = FizzBuzz(10)
        self.assertEqual(result[4], "Buzz")
        self.assertEqual(result[9], "Buzz") 

    def test_returns_fizzbuzz_for_multiples_of_3_and_5(self):
        result = FizzBuzz(15)
        self.assertEqual(result[14], "FizzBuzz") 

    def test_returns_number_for_non_multiples_of_3_and_5(self):
        result = FizzBuzz(6)
        self.assertEqual(result[0], "1")
        self.assertEqual(result[1], "2")
        self.assertEqual(result[3], "4")

    def test_correct_sequence_for_range_1_to_15(self):
        result = FizzBuzz(15)
        expected = ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", 
                    "11", "Fizz", "13", "14", "FizzBuzz"]
        self.assertEqual(result, expected)
