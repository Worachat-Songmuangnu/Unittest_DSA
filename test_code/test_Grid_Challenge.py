import unittest
from production_code.Grid_Challenge import Grid_Challenge

class TestGridChallenge(unittest.TestCase):
    
    def test_sample_case(self):
        grid = ["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]
        self.assertEqual(Grid_Challenge(grid), "YES")
    
    def test_already_sorted(self):
        grid = ["abc", "def", "ghi"]
        self.assertEqual(Grid_Challenge(grid), "YES")

    def test_not_possible(self):
        grid2 = ["xyz", "cba"]
        self.assertEqual(Grid_Challenge(grid2), "NO")
    
    def test_single_row(self):
        grid = ["abc"]
        self.assertEqual(Grid_Challenge(grid), "YES")
    
    def test_smallest_not_possible(self):
        grid3 = ["bc", "ad"]
        self.assertEqual(Grid_Challenge(grid3), "NO")