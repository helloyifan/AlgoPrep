# Wip
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        return
    
    def binarySearch(self, nums, target):
        h, t = 0, len(nums)-1
        while h <= t:
            median = (h + t) //2
            print(median)
            if target > nums[median]:
                h = median + 1

            elif target < nums[median]:
                t = median -1

            else:
                return median
        
        return -1
    
    def binarySearchNotFound(self, nums, h, t, target):
        
        while h <= t:
            median = (h + t) //2

    
sol = Solution()
print(sol.binarySearch([5,7,7,8,8,10], 8))