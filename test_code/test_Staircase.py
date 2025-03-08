import unittest
from production_code.Staircase import staircase

class TestStaircase(unittest.TestCase):
    def test_default_pattern(self):
        expected = "    #\n   ##\n  ###\n ####\n#####\n"
        self.assertEqual(staircase(5), expected)
    
    def test_custom_pattern(self):
        expected = "    *\n   **\n  ***\n ****\n*****\n"
        self.assertEqual(staircase(5, "*"), expected)
    
    def test_n_is_1(self):
        self.assertEqual(staircase(1), "#\n")
    
    def test_n_is_0(self):
        self.assertEqual(staircase(0), "")
    
    def test_n_is_3(self):
        expected = "  #\n ##\n###\n"
        self.assertEqual(staircase(3), expected)
