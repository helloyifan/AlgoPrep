from typing import List
# Time Comp
# O(n)'
# Space
# O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)

        maxRet = 0
        for n in nums:
            curV = n
            curRet = 0
            while curV in hashSet:
                curRet += 1
                curV += 1
            maxRet = max(curRet, maxRet)

        print(maxRet)
        return maxRet
    
sol = Solution()
sol.longestConsecutive([2,20,4,10,3,4,5]) # 4 
sol.longestConsecutive([0,3,2,5,4,6,1,1]) # 7