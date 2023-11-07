from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [None] * len(nums)
        maxVal = float('-inf')
        for i, val in enumerate(nums):
            if (i  == 0 ):
                dp[i] = val
            elif(i == 1):
                dp[i] = max(dp[0], val)
            else:
                dp[i] = max(dp[i-1], dp[i-2]+val)
            maxVal = max(maxVal, dp[i])
        return maxVal


s = Solution()

nums = [1,2,3,1]
r1 = s.rob(nums)
print(r1)

nums2 = [2,7,9,3,1]
r2 = s.rob(nums2)
print(r2)


'''
Other trash tests
[1,2,3,1]
[2,7,9,3,1]
[1]
[1,2]
'''