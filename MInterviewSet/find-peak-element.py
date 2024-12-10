# Notes need to study more, 
# Basically a modified Binary search where we keep trying to find the peak on the side thats greater
# TC: O(logn)
# SC: O(1)
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        
        while l <= r:
            m = (l + r)//2
            # We want to move the right down if the case the number is not smaller
            if m > 0 and nums[m-1] > nums[m]: 
                r = m-1
            # We want to move the left up
            elif m < len(nums)-1 and nums[m+1] >nums[m]:
                l = m + 1
            else: 
                return m
        
        return None


sol = Solution()
print(sol.findPeakElement([1,2,3,1]))
print(sol.findPeakElement([1,2,1,3,5,6,4]))
print(sol.findPeakElement([1]))
print(sol.findPeakElement([1,2]))