# Got it in 20mins,  Needed to scratch by head for the duplicate problem
# Should use debugger to understand why
from typing import List
import copy
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def helper(candidates, target, outputSoFar):
            if target < 0:
                return []
            if target == 0:
                return [outputSoFar]
            
            ret = []
            for i in range(len(candidates)): # not sure about -1
                
                if i > 0:
                    if candidates[i] == candidates[i-1]: # if the number is the same as before, we want to avoid [1,2,2...] case
                        continue

                curNum = candidates[i]
                updatedTarget = target - curNum
                tempOutputSoFar = copy.deepcopy(outputSoFar)
                tempOutputSoFar.append(curNum)
                
                tempRet = helper(candidates[i+1:], updatedTarget, tempOutputSoFar)
                if len(tempRet) > 0:
                    ret = ret + tempRet
            return ret
            

        candidates.sort()
        ret = helper(candidates, target, [])
        #print(ret)

        return ret
    
sol = Solution()
sol.combinationSum2([9,2,2,4,6,1,5], 8)
sol.combinationSum2([1,2,3,4,5], 7)