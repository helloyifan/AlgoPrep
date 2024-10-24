from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        lenCost = len(cost)
        dp = [0 for _ in range(lenCost)]

        i = 0
        while i < lenCost:
            if i == 0 or i == 1:
                dp[i] = 0
            
            stepV = min(dp[i-1], dp[i-2]) + cost[i]
            dp[i] = stepV

            i +=1
        
        ret = None
        if lenCost < 2:
            ret = dp[lenCost-1]
        else:
            ret = min(dp[lenCost-1], dp[lenCost-2])
        
        print(dp)
        print(ret)
        return ret
    


sol = Solution()
sol.minCostClimbingStairs([10,15,20]) # 15
#sol.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]) # 6
