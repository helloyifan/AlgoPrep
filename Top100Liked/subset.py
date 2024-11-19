from typing import List
import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        subsets = [[]]
        currentSubset = []
        def dfs(nums, i): #i to make sure were process same num again
            if i > len(nums)-1:
                return
            currentSubset.append(nums[i]) # add the current num,
            subsets.append(currentSubset[:])
            dfs(nums, i+1)
            currentSubset.pop() # back track cleanup
            dfs(nums, i+1)

        dfs(nums, 0)
        print(subsets)
        return subsets

sol = Solution()
sol.subsets([1,2,3])