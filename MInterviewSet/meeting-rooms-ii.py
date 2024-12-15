# TC: O(nlogn) for processing with heap optimization
# SC: O(n) Heap could be O(n) in worst case
import heapq
from typing import List
class Solution:
    def optimal_heapq_minMeetingRooms(self, intervals: List[List[int]]) -> int:
        meetings = intervals
        meetings.sort() # nlogn
        h = []
        for curMeeting in meetings: # n time
            if len(h) == 0 or curMeeting[0] < h[0]: #Cur meeting starts before earliestEndingMeeting
                heapq.heappush(h, curMeeting[1]) #logn time
            else: # Cur Meeting starts after the earliest ending meeting
                heapq.heappop(h)
                heapq.heappush(h, curMeeting[1])
        return len(h)
    

# TC: Sorting the input  would require nlogn but the processing would  be O(n*n) = O(n^2)
# SC: DP could be one meeting per room in worse case = O(n) 
    def brute_forcemeeting_room_ii(meetings):
        dp = []
        meetings.sort() # we want to sort meetings by start time
        
        for curMeeting in meetings:
            isInserted = False
            for i, existingMeetingEndTime in enumerate(dp):
                if existingMeetingEndTime <= curMeeting[1]:
                    dp[i] = curMeeting[1]
                    isInserted = True
        
            if not isInserted:
                dp.append(curMeeting[1]) # add endtime to the new room

        return len(dp)
