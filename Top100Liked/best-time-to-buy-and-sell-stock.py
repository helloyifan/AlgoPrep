from typing import List
# Time complexity
# O(n*n/2) as constants are ignoredin big O= O(n^2)
# Space complexity
# O(1)
class Solution:
    def on2maxProfit(self, prices: List[int]) -> int:
        lenP = len(prices)

        maxV = 0
        for i in range(lenP):
            for j in range(i, lenP):
                maxV = max(maxV, prices[j] - prices[i])
        print(maxV)
        return maxV

# Optimal Solution:
# Set head to be tail, if tail is ever less then head
# Time Comp
# O(n)
# space comp
# O(1)

    def maxProfit(self, prices: List[int]) -> int:
        h, t = 0, 0
        maxV = 0
        while t < len(prices):
            if prices[h] > prices[t]:
                h =t 
            maxV = max(maxV, prices[t] - prices[h])
            t += 1
        print(maxV)
        return maxV

sol = Solution()
sol.maxProfit([7,1,5,3,6,4])