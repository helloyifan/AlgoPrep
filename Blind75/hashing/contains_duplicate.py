from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)

        prev = ""
        for i, e in enumerate(nums):
            if e == prev:
                return True
            prev = e

        return False

