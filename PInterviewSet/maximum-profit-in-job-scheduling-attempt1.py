# Attempt1: Right idea but too slow
# 
from typing import List
import bisect

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        sortedDS = [] #sorted by start time
        for i in range(len(startTime)):
            sortedDS.append((startTime[i], endTime[i], profit[i])) # tupleFormat: (startime, endtime, profit)
        sortedDS.sort()

        firstStartTime = sortedDS[0][0]

        dp = {} #key: StarTime, value: maxProfit

        for i in range(len(startTime)-1, -1, -1):
            curStartTime = sortedDS[i][0]
            curEndTime = sortedDS[i][1]
            curProfit = sortedDS[i][2]


            sortedDpKeys = sorted(dp.keys())
                
            maxCorrespondingEndtimeProfit = float('-inf')
            maxCorrespondingEndtime = None
            
            for startTimeKey in sortedDpKeys:
                if curEndTime <= startTimeKey:
                    if dp[startTimeKey] > maxCorrespondingEndtimeProfit:
                        maxCorrespondingEndtimeProfit  =  dp[startTimeKey]
                        maxCorrespondingEndtime = startTimeKey
            if maxCorrespondingEndtime != None:
                curProfit += maxCorrespondingEndtimeProfit

            if curStartTime in dp:
                dp[curStartTime] = max(dp[curStartTime], curProfit)
            else:
                dp[curStartTime] = curProfit

        # ret is whatever in dp with maxval
        maxVal = float('-inf')
        for key in dp:
            maxVal = max(maxVal, dp[key])

        print(dp)
        print(maxVal)
        print('----')
        return maxVal
sol = Solution()
#sol.jobScheduling( [1,2,3,3], [3,4,5,6], [50,10,40,70])
# (1,3,50)
# (2,4,10)
# (3,5,40)
# (3,6,70)

sol.jobScheduling( [1,2,3,4,6], [3,5,10,6,9],  [20,20,100,70,60])
sol.jobScheduling([4,2,4,8,2], [5,5,5,10,8], [1,2,8,10,4])