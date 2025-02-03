

from typing import List
from collections import defaultdict

class Solution:
    # Slow backtracking set solution
    # TC: O(len(nums)!) = O(N!)
    # SC: O(len(nums)!) = O(N!)
    def setPermuteUnique(self, nums: List[int]) -> List[List[int]]:
        ret = set()

        def dfs(nums, temp):
            if len(nums) == 0:
                ret.add(tuple(temp[:]))
                return 
            
            for i in range(len(nums)):
                nextNums = nums[:i] + nums[i+1:]
                curNum = nums[i]

                temp.append(curNum)
                dfs(nextNums, temp)
                del temp[-1] # clean up 
        
        dfs(nums, [])

        finRet = []
        for s in ret: # We could have O(N!) rets so, another O(N!) operations here
            finRet.append(list(s))
        print(finRet)
        return finRet

    # Backtracking dd solution
    # count down dd
    # TC:  O(N!)
    # SC: O(N!)
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        dd = defaultdict(int)
        for n in nums:
            dd[n] += 1
        
        def dfs(nums, dd, temp, ret):
            if len(temp) == len(nums):
                ret.append(temp[:])
                return

            for key in dd:
                if dd[key] >0:
                    dd[key] -= 1
                    temp.append(key)

                    dfs(nums, dd, temp, ret)

                    dd[key] += 1
                    temp.pop()
            return

        ret = []
        dfs(nums, dd, [], ret)
        print(ret)
        return ret

sol = Solution()
sol.permuteUnique([1,1,2])
sol.permuteUnique([1,2,3])
