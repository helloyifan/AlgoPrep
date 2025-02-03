# Notes: 
# Airplane im thinking we can keep track of a heap to manage the meetings that will end first
# Once a meeting ends, we pop the next meeting on
# building the result is just to keep track of which rooms meet the max room count condition, and just find the min id

# TC: 
# SC: 
import heapq
from collections import defaultdict
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        print(meetings)
        meetingCounterMap = defaultdict(int)
        meeting_end_time_h = [] # (meetingEndTime, roomId)
        free_h = [] # (roomId)

        # Initalize the rooms
        for room_id in range(n):
            heapq.heappush(free_h, room_id)

        # Process meetings
        for m in meetings:
            meetingStartTime = m[0]
            meetingEndTime = m[1]

            # Basically pop meetings that ended b4 meetingStartTime, and add to heap that
            # prioritzes low roomId
            while len(meeting_end_time_h)> 0 and meetingStartTime >= meeting_end_time_h[0][0]:
                roomMeetingEndTimeThenId = heapq.heappop(meeting_end_time_h)
                roomId = roomMeetingEndTimeThenId[1]
                heapq.heappush(free_h, roomId)

            if len(free_h) > 0:
                roomId = heapq.heappop(free_h)
                heapq.heappush(meeting_end_time_h, (meetingEndTime, roomId))
                meetingCounterMap[roomId] += 1

            else:
                room = heapq.heappop(meeting_end_time_h)
                roomEndTime = room[0]
                roomNum = room[1]

                # If prev meeting ended later
                if roomEndTime > meetingStartTime:
                    meetingEndTime += roomEndTime - meetingStartTime
                    meetingStartTime = roomEndTime

                print(meetingStartTime, meetingEndTime)

                heapq.heappush(meeting_end_time_h, (meetingEndTime, roomNum))
                meetingCounterMap[roomNum] += 1
        
        print(free_h)
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
# sol.mostBooked(2, [[0,10],[1,5],[2,7],[3,4]])
# sol.mostBooked(3, [[1,20],[2,10],[3,5],[4,9],[6,8]])
# sol.mostBooked(4, [[18,19],[3,12],[17,19],[2,13],[7,10]]) # 0 
sol.mostBooked(4, [[48,49],[22,30],[13,31],[31,46],[37,46],[32,36],[25,36],[49,50],[24,34],[6,41]])