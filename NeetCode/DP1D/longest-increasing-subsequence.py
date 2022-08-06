from typing import List

# Todo Revisit this question

# This is a good dp question in the spirit of using the prev results to get the next step
# I struggled with this question conceptually for a whole day lol, 

# Time: O(n^2)
# Space: O(n)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for curInd in range(len(nums)):
            dp.append(1)
            cur = nums[curInd]
            for prevInd in range(curInd):
                prev = nums[prevInd] # check all numbers b4 this

                if (prev < cur and # basically if the current number is smaller then prev Number
                    dp[curInd] < dp[prevInd] + 1):  # and the current MAX number of jumps is lesser then what it could be
                        dp[curInd] = dp[prevInd] + 1  # then update it to what it could be
        #print(dp)
        return max(dp)




s = Solution()

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.


# nums = [10,9,2,5,3,7,101,18]
# r = s.lengthOfLIS(nums)
# print(r)

# nums2 = [0,1,0,3,2,3]
# r2 = s.lengthOfLIS(nums2)
# print(r2)

# nums3 = [7,7,7,7,7,7,7]
# r3 = s.lengthOfLIS(nums3)
# print(r3)

# nums4 = [0]
# r4 = s.lengthOfLIS(nums4)
# print(r4)

# nums5 = [6,5,4,3,2,1]
# r5 = s.lengthOfLIS(nums5)
# print(r5)


# Input
# [0,1,0,3,2,3]
# Expected
# 4
nums6 = [0,1,0,3,2,3]
r6 = s.lengthOfLIS(nums6)
print(r6)

# Input
# [5,7,-24,12,13,2,3,12,5,6,35]
# Expected
# 6

# nums7 = [5,7,-24,12,13,2,3,12,5,6,35]
# r7 = s.lengthOfLIS(nums7)
# print(r7)
