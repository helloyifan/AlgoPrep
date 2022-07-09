from typing import List

# Want to buy at the lowest point
# want to only sell after buying
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowValPtr = None
        highValPtr = None
        maxEarnings = 0

        for i, val in enumerate(prices):
            if (lowValPtr == None):
                lowValPtr = i
            elif(val < prices[lowValPtr]):
                if (highValPtr != None):
            #        print("bought at:", lowValPtr , " sold at: ", highValPtr)
                    maxEarnings = max(maxEarnings, prices[highValPtr]- prices[lowValPtr])
                lowValPtr = i
                highValPtr = None
            elif(val > prices[lowValPtr]):
                if (highValPtr == None or val > prices[highValPtr]):
                    highValPtr = i

            #print("lowValPtr:", lowValPtr , " highValPtr: ", highValPtr)
        
        if (highValPtr != None and lowValPtr != None):
            maxEarnings = max(maxEarnings, prices[highValPtr] - prices[lowValPtr])
        return maxEarnings


s = Solution()

prices = [7,1,5,3,6,4]
r = s.maxProfit(prices)
print(r)


prices2 = [7,6,4,3,1]
r2 = s.maxProfit(prices2)
print(r2)

prices3 = [1, 31]
r3 = s.maxProfit(prices3)
print(r3)
