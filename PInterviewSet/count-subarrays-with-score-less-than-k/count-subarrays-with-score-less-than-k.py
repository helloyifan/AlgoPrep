# Notes: For any staring position l to r,
# where l is always in the result
# there are (r-l+1) subarrays to r

# TC: O(n) this is one pass
# SC: O(1) this constant
from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l, r = 0, 0 
        runningSum = 0
        res = 0
        while r < len(nums):
            runningSum += nums[r]
            while l <= r and runningSum * (r-l+1) >= k: # adjust window until we have another valid range
                runningSum -= nums[l]
                l += 1
            res += (r-l+ 1) # meaning anytime r is moved, #finad all valid subarray of given range, 
            # in a range, theres (r-l+1) unique subarray
            r+=1
        print(res)
        return res

sol = Solution()
sol.countSubarrays([2,1,4,3,5], 10) # 6
sol.countSubarrays([1,1,1], 5) # 5
sol.countSubarrays([1,2,9,1,5],96) # 15
sol.countSubarrays([1,2,3,4],100) # 10


## example [1,2,3,4], k = 100
# 1 # loop 1 res += 1
# 1,2 # loop 2 (accounting for 1,2 and 2) res += 2
# 1,2,3 # loop 3(accounting for 1,2,3 and 2,3 and 3) res += 3
# 1,2,3,4 # loop 4(accounting for 1,2,3,4 and 2,3,4 and 3,4 and 4) res += 4

# Total 10