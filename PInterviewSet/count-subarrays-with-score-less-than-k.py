from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l, r = 0,0
        runningSum = 0
        while l < len(nums) and r < len(nums):
            
            if 
