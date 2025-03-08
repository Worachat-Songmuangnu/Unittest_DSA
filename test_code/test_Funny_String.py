import unittest
from production_code.Funny_String import funnyString

class TestFunnyString(unittest.TestCase):
    
    def test_example_funny(self):
        self.assertEqual(funnyString("acxz"), "Funny")
    
    def test_not_funny(self):
        self.assertEqual(funnyString("abce"), "Not Funny")
    
    def test_single_char(self):
        self.assertEqual(funnyString("a"), "Funny")
    
    def test_two_chars(self):
        self.assertEqual(funnyString("ab"), "Funny")
    
    def test_palindrome(self):
        self.assertEqual(funnyString("racecar"), "Funny")