# Attempt 1 took 40 mins got confused
# Attempt 2 20 mins

# Time Complexity
# Binary search is O(logN) and we execute it twice so still O(logN)

# Space Complexity
# O(c) we are not allocation more space for anything
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        minIndex = self.binarySearchFirst(nums, target)
        if minIndex == -1:
            return [-1, -1]

        maxIndex = self.binarySearchLast(nums, target)
        return [minIndex, maxIndex]
    
    
    def binarySearchFirst(self, nums, target):
        l, r = 0, len(nums) -1
        while l <= r:
            median = (l + r) //2
            if nums[median] < target:
                l = median + 1
            elif target < nums[median]:
                r = median -1
            elif target == nums[median]:
                if median == 0 or nums[median-1] != target:
                    return median
                else:
                    r = median -1
        return -1

    def binarySearchLast(self, nums, target):
        l, r = 0, len(nums) -1
        while l <= r:
            median = (l + r) //2
            if nums[median] < target:
                l = median + 1
            elif target < nums[median]:
                r = median -1 
            elif target == nums[median]:
                if median == len(nums)-1 or nums[median+1] != target:
                    return median
                else:
                    l = median +1 
        return -1

    
sol = Solution()
print(sol.searchRange([5,7,7,8,8,10], 8)) # 3, 4
print(sol.searchRange([5,7,7,8,8,10], 6)) # -1, -1
print(sol.searchRange([2,2], 2)) # 0, 1