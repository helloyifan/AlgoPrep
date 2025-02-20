from typing import List
from collections import defaultdict
import heapq
# Notes: Two heap solution
# TC: Sorting is O(nlogn), rest is heap operations O(logn) and we do it linteraly O(n) so O(nlogn + n*logn) = O(nlogn)
# SC: We maintain heaps, i think they can in theory have every element so O(n)

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        # two heap approach
        freeRooms = []
        roomEndHeap = []
        
        meetingInRoomCounter = defaultdict(int)
        # Step 1. Intalize free rooms
        for i in range(n):
            heapq.heappush(freeRooms, i)

        # Step through the meetings
        for m in meetings:
            meetingStartTime, meetingEndtime = m[0], m[1]

            # Step 2. Try to clean up and rooms based on current start time
            # [0][0] means first meeting on the heap and its meetingEndTimeValue
            while len(roomEndHeap) > 0 and meetingStartTime >= roomEndHeap[0][0]:
                meetingThatJustEnded = heapq.heappop(roomEndHeap)
                meetingThatJustEndedRoom = meetingThatJustEnded[1]
                heapq.heappush(freeRooms, meetingThatJustEndedRoom)

            # Step 3. After cleaning up, if there are any free rooms use it
            if len(freeRooms) > 0:
                curRoom = heapq.heappop(freeRooms)
                heapq.heappush(roomEndHeap,  (meetingEndtime, curRoom))
                meetingInRoomCounter[curRoom] += 1
            # Step 4. If there arenn't any free rooms, then wait for the next room to be free
            else:
                nextMeetingToEnd = heapq.heappop(roomEndHeap)
                nextMeetingToEndEndTime = nextMeetingToEnd[0]
                nextMeetingToEndRoomId = nextMeetingToEnd[1]
                newEndTime = nextMeetingToEndEndTime + (meetingEndtime - meetingStartTime)
                
                newMeetingTuple = (newEndTime, nextMeetingToEndRoomId)
                heapq.heappush(roomEndHeap, newMeetingTuple)

                meetingInRoomCounter[nextMeetingToEndRoomId] += 1

        # Step 5. Build result from default dict
        print(meetingInRoomCounter)
        maxMeetingRoomId = None
        maxMeetinRoomCounter = 0
        for i in range(n):
            if meetingInRoomCounter[i] > maxMeetinRoomCounter:
                maxMeetingRoomId = i
                maxMeetinRoomCounter = meetingInRoomCounter[i]
        print(maxMeetingRoomId)
        return maxMeetingRoomId
    
sol = Solution()
sol.mostBooked(2, [[0,10],[1,5],[2,7],[3,4]])
