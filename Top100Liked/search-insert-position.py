# Notes: The answer is just binary searc result + 1
# TC: O(logn) for binarcy search
# SC: O(1) no additional datastrucutre used
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            median = (l+r)//2
            medianVal = nums[median]
            if medianVal < target:
                l = median + 1
            else:
                r = median - 1
        finMedian = (l+r)//2
        print(finMedian + 1)
        return finMedian + 1