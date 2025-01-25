# Notes: 
# Airplane im thinking we can keep track of a heap to manage the meetings that will end first
# Once a meeting ends, we pop the next meeting on
# building the result is just to keep track of which rooms meet the max room count condition, and just find the min id

# TC: 
import heapq
from collections import defaultdict
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        meetingCounterMap = defaultdict(int)
        h = [] # (meetingEndTime, roomId)

        # Initalize the room
        for i in range(n):
            heapq.heappush(h, (0,i))

        # Process meetings
        for m in meetings:
            room = heapq.heappop(h)
            roomEndTime = room[0]
            roomNum = room[1]

            actualStartTime = m[0]
            actualEndTime = m[1]
            # If prev meeting ended later
            if roomEndTime > actualStartTime:
                actualEndTime += roomEndTime - actualStartTime
                actualStartTime = roomEndTime

            print(actualStartTime, actualEndTime)

            heapq.heappush(h, (actualEndTime, roomNum))
            meetingCounterMap[roomNum] += 1
        
        print(meetingCounterMap)
        
        # Build ret
        maxCount = 0
        maxCountRoomId = None
        for key in meetingCounterMap:
            if meetingCounterMap[key] > maxCount:
                maxCount = meetingCounterMap[key]
                maxCountRoomId = key
            elif meetingCounterMap[key] == maxCount:
                maxCountRoomId = min(maxCountRoomId, key)
        
        print(maxCountRoomId)
        return maxCountRoomId

sol = Solution()
sol.mostBooked(2, [[0,10],[1,5],[2,7],[3,4]])
sol.mostBooked(3, [[1,20],[2,10],[3,5],[4,9],[6,8]])