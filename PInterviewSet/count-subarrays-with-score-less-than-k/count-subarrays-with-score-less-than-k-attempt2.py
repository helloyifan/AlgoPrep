# Attempt 2
# Problem is still O(n^2), i think im missing the point
from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        finRet = 0
        for start in range(len(nums)):
            runningSum = 0
            for end in range(start, len(nums)):
                #print(start, end)
                runningSum += nums[end]
                sizeOfSubArray = (end-start)+1
                if sizeOfSubArray >0 and runningSum < k/sizeOfSubArray:
                    #print(nums[start:end+1], runningSum)
                    finRet += 1
                else:
                    break
        print(finRet)
        return finRet
sol = Solution()
sol.countSubarrays([2,1,4,3,5], 10) # 6
sol.countSubarrays([1,1,1], 5) # 5
# sol.countSubarrays([1,2,9,1,5],96) # 15