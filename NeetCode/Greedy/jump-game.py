from typing import List

class Solution:
    # The trick with this type of problem is that if u can get to X, then 
    # You can get too all precedent of X
    def canJump(self, nums: List[int]) -> bool:

        # You are initially positioned at the array's first index,
        maxDis = 0 
        for i, val in enumerate(nums):
            if (i > maxDis):
                return False

            maxDis = max(maxDis, i + val)

        # Return true if you can reach the last index, or false otherwise.
        if (maxDis >= len(nums) - 1):
            return True
        return False


s = Solution()


nums = [2,3,1,1,4]
r = s.canJump(nums)
print(r)
print('---')

nums2 = [3,2,1,0,4]
r2 = s.canJump(nums2)
print(r2)
print('---')

nums3 = [2,3,3,0,0]
r3 = s.canJump(nums3)
print(r3)
print('---')

nums4 = [0]
r4 = s.canJump(nums4)
print(r4)
print('---')
