# Solved in 15 min from intuition
# But starting starting from subset 1 
# What i did was i just added a sort and did a check to see if the list in already in the ret
# im not sure sure if this is the intetion of the question 
from typing import List
import copy

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        def helper(nums):
            if len(nums) == 0:
                return [[]]
            

            curRet = helper(nums[:-1])
            curRetCopy = copy.deepcopy(curRet)
            
            for i in curRetCopy:
                temp = i
                temp.append(nums[-1])
                if not temp in curRet:
                    curRet.append(temp)
            return curRet
        
        ret = helper(nums)
        #print(ret)
        return ret

if __name__ == '__main__':
    sol = Solution()
    sol.subsetsWithDup([1,2,1])
    sol.subsetsWithDup([7,7])
    