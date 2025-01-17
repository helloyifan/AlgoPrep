from typing import List
import bisect

# Bottom up solution
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)

        data = []
        for i in range(n):
            data.append((startTime[i], endTime[i], profit[i]))
        
        # we sort by endtime, so we can always take the prev element
        # if we sort by start time, we cant take prev element (bcuz it might not have ended yet)
        data.sort(key=lambda x:x[1])
        print(data)

        dp = [0 for i in range(n)]

        for i in range(n):
            curStartTime = data[i][0]
            curEndTime = data[i][1]
            curProfit = data[i][2]
            
            maxPrevIndex = self.binsearch(0, i, data, curStartTime)
            if maxPrevIndex != -1:
                maxPrevProfit = dp[maxPrevIndex]    
                curProfit += maxPrevProfit            

            if i > 0:
                dp[i] = max(curProfit, dp[i-1])
            elif i == 0:
                dp[i] = curProfit

        ret = dp[-1]
        print(dp)
        print(ret)
        return ret

    # Modified binsearch to find the best match,
    # Basically this will find the closest value that is smaller to the target
    def binsearch(self, minV, maxV, data, target):
        l, r = minV, maxV
        best = -1  # Keep track of the best valid index

        while l <= r:
            m = (l + r) // 2
            if data[m][1] <= target:  # If the job's end time <= target, it's valid
                best = m
                l = m + 1  # Try to find a later job
            else:  # If the job's end time > target, move left
                r = m - 1

        return best

sol = Solution()
sol.jobScheduling( [1,2,3,3], [3,4,5,6], [50,10,40,70]) #120
# (1,3,50)
# (2,4,10)
# (3,5,40)
# (3,6,70)

# sol.jobScheduling( [1,2,3,4,6], [3,5,10,6,9],  [20,20,100,70,60]) #150
# sol.jobScheduling([4,2,4,8,2], [5,5,5,10,8], [1,2,8,10,4])
