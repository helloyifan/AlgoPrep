import math
from typing import List

# Fun question
# Ancedote, we need to see if our current eating rate is fast enough for the time we have
# if its too fast or too slow use binary search to find best speed

class Solution:
    ## Bruteforce
    def bruteForce(self, piles: List[int], h: int) -> int:
        curEatingRate = 0
        while True:
            curEatingRate += 1
            totalTimeForThisRate = 0 
            for pile in piles:
                totalTimeForThisRate += math.ceil(pile/curEatingRate)
            
            if totalTimeForThisRate <= h:
                return curEatingRate
            
        return -1
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        curEatingRate = 0
        f, b = 1, max(piles)
        minEatingRate = float("inf")
        while f <= b:
            curEatingRate = self.curEatRateByBinarySearch(f,b)
            totalTimeForThisRate = 0 
            
            for pile in piles:
                totalTimeForThisRate += math.ceil(pile/curEatingRate)
            
            if totalTimeForThisRate <= h: # beat the time
                b = curEatingRate -1 # could use less eating rate
                minEatingRate = min(minEatingRate, curEatingRate)
            else:
                f = curEatingRate + 1 # need more eating rate
            
        return minEatingRate
    
    def curEatRateByBinarySearch(self, f ,b):
        return math.ceil((f + b)/2)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.minEatingSpeed([1,4,3,2], 9))
    print(sol.minEatingSpeed([25,10,23,4], 4))
    print(sol.minEatingSpeed([312884470], 968709470))
