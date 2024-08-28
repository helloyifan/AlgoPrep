from typing import List

# non dp recursive solution
# took like 10 mins to code out
class Solution:
    # this will take a time of 2^n
    def nonDPRecursiveSolution(self, nums: List[int], target: int) -> int:
        # subNum bcuz we take element from the front every time
        # not very efficient
        def helper(subNums, sumV, target):
            targetSum = 0
            if len(subNums) == 0:
                if sumV == target:
                    targetSum += 1 
                return targetSum

            curNum = nums[0]

            targetSum += helper(subNums[1:], sumV + curNum, target)
            targetSum += helper(subNums[1:], sumV - curNum, target)        
            return targetSum
        
        ret = helper(nums, 0, target)
        print(ret)
        return ret 
    
    # Solution with memoization that uses index instead of a sublist
    
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def helper(index: int, sumV: int) -> int:
            targetSum = 0

            # Memoize 
            if (index, sumV) in dp:  # Key is a tuple instead of a list
                return dp[(index, sumV)]
            
            # Base case 
            if (index == len(nums)):
                if sumV == target:
                    targetSum += 1
                dp[(index, sumV)] = targetSum
                return targetSum

            targetSum += helper(index+1, sumV + nums[index])
            targetSum += helper(index+1, sumV - nums[index])

            dp[(index, sumV)] = targetSum
            return targetSum

        ret = helper(0, 0)
        print(ret)
        return ret
    
if __name__ == "__main__":
    sol = Solution()
    sol.findTargetSumWays([2,2,2], 2)