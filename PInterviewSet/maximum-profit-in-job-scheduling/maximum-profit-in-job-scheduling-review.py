from typing import List
# Use DP to store max value at every i
# Ues binsearch to decide which prev dp is usable 
# We use the right most index, wheere the endtime is <= the target

# TC: preporcess O(n), sort O(nlogn), forloop is O(n), binsearch is O(logn) but called n times, Total:  O(nlogn)
# SC: ds is O(n)
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        ds = []
        for i in range(n):
            ds.append((startTime[i], endTime[i], profit[i]))

        ds.sort(key= lambda x: x[1]) # Sort my end time
        
        dp = [0 for _ in range(n)] # DP is the same size as DS, DP  represents the most amount of money you can make up to that point

        for i in range(n):
            curStartTime = ds[i][0]
            curEndTime = ds[i][1]
            curProfit = ds[i][2]

            # Heres the fked up part,
            # We pass in DS, which is [(start, end, profit)]
            # And we use the index determined there, and map it back to DP for getting the max Value
            # Because the value in DP is the money you can make until that point

            prevMaxProfitIndex = self.binSearchLeft(ds, curStartTime) # find the most money you can make
            if prevMaxProfitIndex != -1:
                prevMaxProfitVal = dp[prevMaxProfitIndex] # noticed its DP here, but we use the index from DS its fked up
                curProfit += prevMaxProfitVal
            
            if i > 0:
                dp[i] = max(dp[i-1], curProfit)
            else:
                dp[i] = curProfit

        print(ds)
        print(dp)
        ret = dp[-1]
        return ret
    # Find first value to the left
    # biggestIdxSmallerThanOfEqualTarget
    def binSearchLeft(self, nums, target):
        l, r= 0, len(nums) -1
        biggestIdxSmallerThanOfEqualTarget = -1

        while l <= r:
            med = (l + r) //2
            
            #if nums[med] <= target:
            if nums[med][1] <= target: # we using [1] for starttime
                biggestIdxSmallerThanOfEqualTarget = med
                l = med +1
            else: # nums[med] > target:
                r = med -1
           
        return biggestIdxSmallerThanOfEqualTarget
    
sol = Solution()

# print(sol.binSearchLeft([1,1,2,3,5,7], 5))
# print(sol.binSearchLeft([1,1,2,3,5,7], 6))

#print(sol.jobScheduling([1,2,3,3], [3,4,5,6], [50,10,40,70])) # 120
print(sol.jobScheduling([1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60])) # 150