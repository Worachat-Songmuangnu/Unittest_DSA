import unittest
from production_code.Two_Characters import Two_Characters

class TestTwoCharacters(unittest.TestCase):

    def test_example_input(self):
        self.assertEqual(Two_Characters('beabeefeab'), 5)

    def test_single_character(self):
        self.assertEqual(Two_Characters('aaaaa'), 0)

    def test_multiple_distinct_characters(self):
        self.assertEqual(Two_Characters('abcde'), 0)

    def test_valid_alternating(self):
        self.assertEqual(Two_Characters('ababab'), 6)

    def test_valid_with_mixed_characters(self):
        self.assertEqual(Two_Characters('xyxyxyxy'), 8)
