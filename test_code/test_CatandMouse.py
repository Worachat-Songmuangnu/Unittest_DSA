import unittest
from production_code.CatandMouse import CatandMouse
class TestCatAndMouse(unittest.TestCase):

    def test_mouse_escapes_when_both_cats_are_equal_distance(self):
        self.assertEqual(CatandMouse(2, 4, 3), "Mouse C")

    def test_cat_a_reaches_mouse_first(self):
        self.assertEqual(CatandMouse(1, 5, 2), "Cat A")

    def test_cat_b_reaches_mouse_first(self):
        self.assertEqual(CatandMouse(3, 6, 5), "Cat B")

    def test_mouse_between_cats_and_escapes(self):
        self.assertEqual(CatandMouse(5, 9, 7), "Mouse C")

    def test_cat_a_wins_when_mouse_near_to_cat_a(self):
        self.assertEqual(CatandMouse(10, 20, 11), "Cat A")

