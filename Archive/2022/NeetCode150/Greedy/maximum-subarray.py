from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Figure out the max value at index i, so you can figure out the max calculate and index i+1
        
        totalMaxVal = float('-inf')
        prevMaxVal = float('-inf')
        for i, e in enumerate(nums):
            prevMaxVal = self.helper(prevMaxVal, nums, i)
            totalMaxVal = max(totalMaxVal, prevMaxVal)
        return totalMaxVal

    def helper(self, prevMaxVal: int, nums: List[int], curIndex: int ) -> int:
        curVal = nums[curIndex]
        ret = max(prevMaxVal + curVal, curVal)
        #print("ret: ", ret , "prevMaxVal + curVal:" ,prevMaxVal + curVal, "curVal", curVal)
        return ret


sol = Solution()
nums1 = [-2,1,-3,4,-1,2,1,-5,4]
r1= sol.maxSubArray(nums1)
print(r1)
