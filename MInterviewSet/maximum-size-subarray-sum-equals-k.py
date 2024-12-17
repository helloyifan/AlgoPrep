# Notes: Running sum, save every iteration of it to a hashmap to lookback for it

# TC: O(n) for the iteratior
# SC: O(n) for sumToLoc
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        runningSum = 0
        maxLength = 0
        sumToLoc = {} # sum : location
        for i in range(len(nums)):
            runningSum += nums[i]
            if not runningSum in sumToLoc:
                sumToLoc[runningSum] = i

            if runningSum == k: # if we are able to find k
                maxLength = max(maxLength, i +1 )
            elif runningSum - k in sumToLoc: # if we are able to find diff between k and running sum,
                maxLength = max(maxLength, i - sumToLoc[runningSum - k])

        return maxLength