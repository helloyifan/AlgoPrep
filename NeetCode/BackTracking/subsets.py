from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        self.helper(nums, output)
        return output

    def helper(self, nums, output):
        while len(nums) > 0:
            frontNumber = nums.pop(0)
            newEntries = []
            for j, val in enumerate(output):
                copy = val.copy()
                copy.append(frontNumber)
                newEntries.append(copy)

            output.extend(newEntries)
        return

'''

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
'''

s = Solution()
nums1 = [1,2,3]
r1 = s.subsets(nums1)
print(r1)

nums2 = [0]
r2 = s.subsets(nums2)
print(r2)

nums3 = [0,1,2,3,4,5,6,7,8,9]
r3 = s.subsets(nums3)
print(r3)
