import unittest
from production_code.alternating_Characters import alternating_Characters

class TestAlternatingCharacters(unittest.TestCase):
    
    def test_all_same_chars(self):
        self.assertEqual(alternating_Characters("AAAA"), 3)
    
    def test_alternating_perfect(self):
        self.assertEqual(alternating_Characters("ABABAB"), 0)
    
    def test_mixed_groups(self):
        self.assertEqual(alternating_Characters("AAABBB"), 4)
    
    def test_single_char(self):
        self.assertEqual(alternating_Characters("A"), 0)
    
    def test_two_chars_repeated(self):
        self.assertEqual(alternating_Characters("AA"), 1)