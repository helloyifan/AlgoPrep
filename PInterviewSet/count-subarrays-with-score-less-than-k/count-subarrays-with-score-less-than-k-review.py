# Notes: Two pointer question
# Score is `score = runningSum * (r-l)`
# We add (r-l) to ret if score is less than k
# TC: O(n)
# SC: O(1)
from typing import List
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l, r = 0, 0 

        runningSum = 0
        ret = 0
        # score = runningSum * (r-l)
        while r < len(nums):
            runningSum += nums[r]
            r += 1
            while (runningSum * (r-l)) >= k:
                runningSum -= nums[l]
                l+= 1
            ret += r-l
        return ret
    
sol = Solution()
print(sol.countSubarrays([2,1,4,3,5],  10))
print(sol.countSubarrays([1,1,1],  5))
