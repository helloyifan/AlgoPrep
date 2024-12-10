# Solved in 15 min, mostly from intuation
# The ret = ret + curret is sus but maybe its okay

# Time Complexity
# For every level at DFS, we perform O(n!) operations
# 3*2*1

# Space Complexity
# 
from typing import List
import copy
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def helper(nums):
            if len(nums) == 1:
                return [[nums[0]]]
            ret = []
            for i, e in enumerate(nums):
                cur = copy.deepcopy(nums)
                cur.pop(i)
                curRet = helper(cur)
                for singlePermutation in curRet:
                    singlePermutation.append(e)

                ret = ret + curRet # this seems sus
            return ret 
        
        ret = helper(nums)
        #print(ret)
        return ret

if __name__ == '__main__':
    sol = Solution()
    sol.permute([1,2,3])
    sol.permute([7])

# 1 2 3
# 1 2 -> 3
# 1 -> 2
# 2 -> 1

# 1 3 -> 2
# 1 -> 3
# 3 -> 1

# 2 3 -> 1
# 2 -> 3
# 3 -> 2