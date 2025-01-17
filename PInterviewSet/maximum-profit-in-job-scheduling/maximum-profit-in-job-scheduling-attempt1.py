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

        dp = {} #key: StarTime, value: maxProfit

        for i in range(len(startTime)-1, -1, -1):
            curStartTime = sortedDS[i][0]
            curEndTime = sortedDS[i][1]
            curProfit = sortedDS[i][2]

            sortedDpKeys = sorted(dp.keys())
                
            maxCorrespondingEndtimeProfit = float('-inf')
            maxCorrespondingEndtime = None
           
            startPos = self.binarySearchToFindFirstGreaterThanValue(curEndTime, sortedDpKeys)
            # print(sortedDpKeys)
            # print(startTimeKey)
            for startTimeKey in sortedDpKeys[startPos:]:
                if curEndTime <= startTimeKey:
                    if startTimeKey in dp and dp[startTimeKey] > maxCorrespondingEndtimeProfit:
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

    def binarySearchToFindFirstGreaterThanValue(self, target, nums):
        left, right = 0, len(nums)
        result = -1  # Default if no element is greater than the target

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                result = mid  # Potential candidate
                right = mid  # Move left to find the first occurrence
            else:
                left = mid + 1  # Move right

        return result
sol = Solution()
sol.jobScheduling( [1,2,3,3], [3,4,5,6], [50,10,40,70])
# (1,3,50)
# (2,4,10)
# (3,5,40)
# (3,6,70)

# sol.jobScheduling( [1,2,3,4,6], [3,5,10,6,9],  [20,20,100,70,60])
# sol.jobScheduling([4,2,4,8,2], [5,5,5,10,8], [1,2,8,10,4])


# print(sol.binarySearchToFindFirstGreaterThanValue(3, [0,1,2,5]))