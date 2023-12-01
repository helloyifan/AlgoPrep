from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        for i, e in enumerate(nums):
            f = i + 1
            b = len(nums) -1

            while (f < b):
                sum3Numbers = nums[i] + nums[f] + nums[b]

                if (sum3Numbers < 0 ):
                    f = f + 1
                elif (sum3Numbers > 0):
                    b = b - 1
                else: # implict if sum3Numbers == 0
                    triplet = [nums[i], nums[f], nums[b]]
                    ret.append(triplet) if (not triplet in ret) else None
                    b = b - 1 # This doesnt matter, just gotta move somethign
        return ret

sol = Solution()
nums1 = [-1,0,1,2,-1,-4]
r1 = sol.threeSum(nums1)
print(r1)

nums2 = [0,1,1]
r2 = sol.threeSum(nums2)
print(r2)

nums3 = [0,0,0]
r3 = sol.threeSum(nums3)
print(r3)
