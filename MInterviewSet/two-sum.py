# TC: O(n) one pass at most
# SC: O(n) for each item it can exist in dict

from typing import List

class Solution:
    def hashtwoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, n in enumerate(nums):
            if n in h:
                return [h[n], i]
            h[target-n] = i
        return None
    # Brute force 
    # TC: O(n^2)
    # SC: O(1)
    def bruteForcetwoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None

    # Two Pointers
    # TC: O(nlogn) due to sorting
    # SC:O(1)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = []
        for i, e in enumerate(nums):
            h.append((i,e))

        sortedList = sorted(h, key = lambda x:x[1])
        #print(sortedList)
        l, r = 0 , len(nums)-1

        while l < r:
            cur = sortedList[l][1] + sortedList[r][1]
            if cur < target:
                l += 1
            elif cur > target:
                r -= 1
            else:
                return [sortedList[l][0], sortedList[r][0]]


sol = Solution()
#print(sol.twoSum([2,7,11,15], 9))
print(sol.twoSum([3,2,4], 6))