from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c = {}
        for i, val in enumerate(nums):
            if (val in c):
                return [c[val], i]

            c[target - val] = i
        return None


##
s = Solution()

nums = [2,7,11,15]
target = 9

r = s.twoSum(nums, target)
print (r)

nums2 = [3,2,4]
target2 = 6
r2 = s.twoSum(nums2, target2)
print (r2)

nums3 = [3,3]
target3 = 6
r3 = s.twoSum(nums3, target3)
print(r3)