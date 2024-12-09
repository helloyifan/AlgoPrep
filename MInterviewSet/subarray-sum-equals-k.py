# Notes:
# Sliding window doesn't work if values are both negative and positive, spend 20 mins trying
# Intuition:
# prefix_sum 10 and prefix_sum 15 have a difference of 5, meaning there was a subarray sum of 5
# TC: O(n)
# SC: O(n) for defaultdict
from typing import List
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_dict = defaultdict(int) 
        # 0:1, To handle subarray that starts from the beginning (prefix_sum start at 0)
        prefix_sum_dict[0] = 1
        prefix_sum = 0
        retCount = 0
        for n in nums:
            prefix_sum += n
            # Something thats k away from current means it a valid subarray sum
            if (prefix_sum - k) in prefix_sum_dict:
                retCount += prefix_sum_dict[prefix_sum - k]
            prefix_sum_dict[prefix_sum] +=1
        print(retCount)
        return retCount
sol = Solution()
sol.subarraySum([1,1,1], 2) # 2
sol.subarraySum([-1,-1,1], 0) # 1
sol.subarraySum([1,-1,0], 0) # 3


# Setting prefix_sum_dict[0] = 1 ensures that if the sum of a 
# subarray starting from the very beginning of the array equals 𝑘
# it gets counted. 
# Without it, you would miss subarrays like 
# [nums[0], nums[1], ..., nums[i]] where the total sum is k






