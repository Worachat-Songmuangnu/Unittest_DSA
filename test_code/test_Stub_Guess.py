import unittest
from unittest.mock import patch
from production_code.Guess import guess_int,guess_float

class TestStubGuessFunctions(unittest.TestCase):
    
    @patch('production_code.Guess.randint')
    def test_guess_int(self, mock_randint):
        mock_randint.return_value = 5

        result = guess_int(1, 10)
        self.assertEqual(result, 5)
        mock_randint.assert_called_once_with(1, 10)
    
    @patch('production_code.Guess.uniform')
    def test_guess_float(self, mock_uniform):
        mock_uniform.return_value = 3.14

        result = guess_float(1.0, 5.0)
        self.assertEqual(result, 3.14)
        mock_uniform.assert_called_once_with(1.0, 5.0)
    
    @patch('production_code.Guess.randint')
    def test_guess_int_range(self, mock_randint):
        mock_randint.return_value = 7

        result = guess_int(5, 10)
        self.assertEqual(result, 7)
        self.assertTrue(5 <= result <= 10)
    
    @patch('production_code.Guess.uniform')
    def test_guess_float_range(self, mock_uniform):
        mock_uniform.return_value = 2.5

        result = guess_float(1.0, 3.0)
        self.assertEqual(result, 2.5)
        self.assertTrue(1.0 <= result <= 3.0)
    
    @patch('production_code.Guess.randint')
    def test_guess_int_multiple_calls(self, mock_randint):
        mock_randint.side_effect = [3, 8, 1]

        self.assertEqual(guess_int(1, 10), 3)
        self.assertEqual(guess_int(1, 10), 8)
        self.assertEqual(guess_int(1, 10), 1)
        self.assertEqual(mock_randint.call_count, 3)
