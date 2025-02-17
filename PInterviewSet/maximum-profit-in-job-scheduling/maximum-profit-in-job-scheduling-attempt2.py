from typing import List

# Notes: I fucked up the top down solution, need to try agian later
# Use DP to store max value at every i
# Ues binsearch to decide which prev dp is usable 
# We use the right most index, wheere the endtime is <= the target

# TC: preporcess O(n), sort O(nlogn), forloop is O(n), binsearch is O(logn) but called n times, Total:  O(nlogn)
# SC: ds is O(n)

# Bottom up solution
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        ds = []

        for i in range(n):
            ds.append((startTime[i],endTime[i],profit[i]))
        
        ds.sort(key=lambda x: x[1]) # sort by end time
        print(ds)

        # The DP is, from the current index
        # use binsearch to indentify which prev index we can use
        # We use the right most index, wheere the endtime is <= the target
        dp = [0 for i in range(n)]

        for i in range(n):
            curStartTime = ds[i][0]
            curEndTime = ds[i][1]
            curProfit = ds[i][2]
            
            maxPrevIndex = self.binsearchLeft(curStartTime, ds)
            if maxPrevIndex != -1:
                maxPrevProfit = dp[maxPrevIndex]
                curProfit += maxPrevProfit

            if i > 0:
                dp[i] = max(curProfit, dp[i-1])
            else:
                dp[i] = curProfit

        ret = dp[-1]
        print(dp)
        print(ret)
        return ret
    
    def binsearchLeft(self, target, ds):
        l, r = 0, len(ds)-1

        # For this question, we want to find
        # The biggest (right most index) that is <= to the target
        biggestIndexSmallerThenTarget = -1
        while l <= r:
            med = (l+r)//2
            val = ds[med][1] # end times

            if target == val:
                biggestIndexSmallerThenTarget = med
                l = med + 1
            elif val < target :
                biggestIndexSmallerThenTarget = med
                l = med + 1
            elif val > target:
                r = med -1
            else:
                raise("something went wrong")

        return biggestIndexSmallerThenTarget # The first value thats bigger than target
    
sol = Solution()
sol.jobScheduling( [1,2,3,3], [3,4,5,6], [50,10,40,70]) #120
sol.jobScheduling( [1,2,3,4,6], [3,5,10,6,9],  [20,20,100,70,60]) #150
# sol.jobScheduling([4,2,4,8,2], [5,5,5,10,8], [1,2,8,10,4])
