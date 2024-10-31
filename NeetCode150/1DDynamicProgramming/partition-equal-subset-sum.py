from typing import List

# Attempt 1, passed on neetcode but not ideal soltuon
# Attempt 1 also passed on leetcode so idk
# Runtime is O(n*2^n)
# space is O(2^n)

class Solution:
    def canPartitionAttempt1(self, nums: List[int]) -> bool:
        if sum(nums)%2 ==1: # odd numbers can't be split in tow
            return False
        
        half = sum(nums)//2 # if we can get half, then it means the other half is the same sum
        
        dp = {}

        for n in nums: #O(n)
            # if the one element in n happens to be half
            if n == half:
                return True

            addToDp = []
            # check through ur list to see if theres 
            # an existing sum we can reuse to hit half
            for key in dp: # This loop sucks thou its O(2^n)
                newVal = key+n
                if newVal == half:
                    return True
                addToDp.append(newVal)# We are always storing so O(2^n)
            for i in addToDp:
                dp[i]= True
            dp[n] = True

        return False


sol = Solution()
print(sol.canPartition([1,2,3,4])) # true
print(sol.canPartition([1,2,3,4,5])) # false
# print(sol.canPartition([1,2,3,4,8])) # true
# print(sol.canPartition([1,2,3,4,12])) # false
print(sol.canPartition([1,1])) # false


# 1 2 3 4
# 10
# 5

# Using not all the elemntst to reach half is good

# Using all the element is bad
