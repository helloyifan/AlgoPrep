# Attempt 1: Good try but too slow!
# TC: O(n^2)
from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        totalRetCount = 0
        for i in range(1, len(nums)+1):
            totalRetCount += self.countSubArrayUnderTargetSum(nums, i, k/i)

        print('totalRetCount:', totalRetCount)
        return totalRetCount
    
    def countSubArrayUnderTargetSum(self, nums, size, targetSum):
        l,r = 0, size
        runningSum = 0
        # Load up the numbers
        for i in range(size):
            runningSum += nums[i]

        finalRet = 0

        if runningSum < targetSum:
            print(nums[l:r], runningSum)
            finalRet += 1

        while r < len(nums):
            runningSum -= nums[l]
            l += 1
            runningSum += nums[r]
            r += 1

            if runningSum < targetSum:
                print(nums[l:r], runningSum)
                finalRet += 1

        print(finalRet)
        return finalRet

sol = Solution()
# sol.countSubarrays([2,1,4,3,5], 10)
# sol.countSubarrays([1,1,1], 5)
sol.countSubarrays([1,2,9,1,5],96)

## Debugging
# sol.countSubArrayUnderTargetSum([2,1,4,3,5], 1, 6)
# sol.countSubArrayUnderTargetSum([2,1,4,3,5], 2, 6)
# sol.countSubArrayUnderTargetSum([2,1,4,3,5], 3, 6)