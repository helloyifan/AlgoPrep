# TC: O(2^n) we make n decisions twice, 
# However with memoization the DP if bound by O(sum*n)
    # sum is the sum of the absolute values of all elements in nums because runningSum can range from -sum to sum.
# SC: O(n⋅sum)  items are written to DP List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        def dfs(nums, ptr, runningSum, target, dp):
            if (ptr, runningSum) in dp:
                return dp[(ptr, runningSum)]
            
            if len(nums) == ptr:
                if runningSum == target:
                    return 1
                else:
                    return 0
            
            curLevelRet = 0
            curLevelRet += dfs(nums, ptr+1, runningSum + nums[ptr], target, dp)
            curLevelRet += dfs(nums, ptr+1, runningSum - nums[ptr], target, dp)
            
            dp[(ptr, runningSum)] = curLevelRet
            return curLevelRet
        
        ret = dfs(nums, 0, 0, target, {})
        return ret