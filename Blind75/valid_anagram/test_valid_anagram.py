import unittest
from valid_anagram import Solution

class Test_ValidAnagram(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_testone(self):
        s = 'anagram'
        r = 'nagaram'
        result = self.solution.isAnagram(s, r)
        self.assertTrue(result, "This is right")

if __name__ == "__main__":
    unittest.main()