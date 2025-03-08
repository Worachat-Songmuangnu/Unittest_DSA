import unittest
from production_code.Caesar_Cipher import Caesar_Cipher

class TestCaesarCipher(unittest.TestCase):
    
    def test_sample_case(self):
        self.assertEqual(Caesar_Cipher("middle-Outz", 2), "okffng-Qwvb")
    
    def test_no_rotation(self):
        self.assertEqual(Caesar_Cipher("Hello", 0), "Hello")
    
    def test_full_rotation(self):
        self.assertEqual(Caesar_Cipher("abc", 26), "abc")
    
    def test_special_chars(self):
        self.assertEqual(Caesar_Cipher("a-b-c", 1), "b-c-d")
    
    def test_large_shift(self):
        self.assertEqual(Caesar_Cipher("xyz", 27), "yza")