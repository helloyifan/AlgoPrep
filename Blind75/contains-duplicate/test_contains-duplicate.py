import unittest
from contains_duplicate import Solution

class TestContainsDuplicate(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_no_duplicates(self):
        nums = [1, 2, 3, 4, 5]
        result = self.solution.containsDuplicate(nums)
        self.assertFalse(result, "No duplicates should be found")

    def test_with_duplicates(self):
        nums = [1, 2, 3, 3, 4, 5]
        result = self.solution.containsDuplicate(nums)
        self.assertTrue(result, "Duplicates should be found")

    def test_empty_list(self):
        nums = []
        result = self.solution.containsDuplicate(nums)
        self.assertFalse(result, "Empty list should not contain duplicates")

if __name__ == "__main__":
    unittest.main()