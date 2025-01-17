# Notes: Not sure if theres a more brute force approac
# The max heap approach is clever,
# Basically you dont want to write the most occuring character twice
# So you can address with a list 
# TC: Total O(nlogn): build DP is O(n) time, processing main for loop is done n times (write one letter at a time)
# heappush and pop is O(logn) and we perform those operation n times
# SC: O(n) for DP and heap data structures
from collections import defaultdict
class Solution:
    def reorganizeString(self, s: str) -> str:
        numOfChars = 0
        ret = ''

        dp = defaultdict(int)
        for c in s:
            dp[c]+=1

        h = []

        #setup a max heap to use it letters first
        for key in dp:
            heapq.heappush(h, (-1*dp[key], key))

        prevTempHolder = None
        while len(h) > 0:
            cur = heapq.heappop(h)
            curKeyChar = cur[1]

            ret += curKeyChar

            if prevTempHolder != None:
                # Push the temp on the heap
                # Adjust the count occurance
                adjustedPrevCount = prevTempHolder[0] + 1
                prevKey = prevTempHolder[1]
                # This is necessary to prevent the same letter twice
                if adjustedPrevCount < 0: # lesser than bcuz max heap negative
                    heapq.heappush(h, (adjustedPrevCount, prevKey))

            prevTempHolder = cur
        
        if len(ret) != len(s):
            return ''

        return ret
