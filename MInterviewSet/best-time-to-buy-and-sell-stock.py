from typing import List
from collections import deque
def o2n_maxProfit(prices: List[int]) -> int:
    
    # preprocessing time
    sellTimePriceMax = deque([])
    maxStockPriceSoFar = float('-inf')
    for i in range(len(prices)-1, -1, -1):
        maxStockPriceSoFar = max(maxStockPriceSoFar, prices[i])
        sellTimePriceMax.appendleft(maxStockPriceSoFar)
    
    print(sellTimePriceMax)
    maxProfit = float('-inf') 
    # generate the max profit
    for i, p in enumerate(prices):
        maxProfit = max(maxProfit, sellTimePriceMax[i] - prices[i])
    print(maxProfit)                                                        
    return maxProfit


def maxProfit(prices: List[int]) -> int:
    minBuyPrices = float('inf')
    maxProfit = float('-inf')
    for i, p in enumerate(prices):
        minBuyPrices = min(minBuyPrices, p)
        maxProfit = max(maxProfit, p - minBuyPrices)
    print(maxProfit)
    return maxProfit

# TC:O(n)+ O(n) we do two passes = O(2(n))
# Better solution does it in O(n)
# SC: O(n) sellTimePriceMax will grow in the same rate as input
