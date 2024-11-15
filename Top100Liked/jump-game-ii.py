# Time Comp
# O(n) - usecase [1,1,1,1,1,1]
# Space Complexity 
# O(1)

from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        # Handles edge case
        l, r=  0, 0 
        numOfJumps = 0

        while r < len(nums)-1:
            furtherest = 0
            for i in range(l, r+1):
                furtherest = max(furtherest, i + nums[i]) # we always jump as far as we can

            r = furtherest
            l += 1 # we can always jump one step
            numOfJumps +=1

        return numOfJumps
 
sol = Solution()
print(sol.jump([2,3,1,1,4])) # 2
print(sol.jump([2,3,0,1,4])) # 2 
print(sol.jump([1])) # 0
print(sol.jump([3,4,3,2,5,4,3]))# 3
print(sol.jump([1,2]))# 1
print(sol.jump([1,2,3]))# 2

print(sol.jump([1,2,1,1,1])) # 3
