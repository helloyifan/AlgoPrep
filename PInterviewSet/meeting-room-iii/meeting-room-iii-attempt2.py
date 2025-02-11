# Notes: the part that got me tricked up was, if hteres no free rooms, then pop up a room from the roomEndHeap
# TC: Sorting is O(nlogn), rest is heap operations O(logn) and we do it linteraly O(n) so O(nlogn + n*logn) = O(nlogn)
# SC: We maintain heaps, i think they can in theory have every element so O(n)

from typing import List
import heapq
from collections import defaultdict
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        roomEndHeap = []
        freeRooms = []

        retRoomMeetingsCounter = defaultdict(int)
        print(meetings)
        # Initalization, just pushing the rooms to the heap
        for i in range(n):
            heapq.heappush(freeRooms, i)

        for m in meetings: # Assuming meeting rooms are sorted by endtime
            meetingStartTime, meetingEndTime = m[0], m[1]

            while len(roomEndHeap) > 0 and meetingStartTime >= roomEndHeap[0][0]: #[0][0] means first meeting on the heap and its meetingEndTimeValue
                meetingThatJustEnded = heapq.heappop(roomEndHeap)
                meetingThatJustEndedRoom = meetingThatJustEnded[1]
                heapq.heappush(freeRooms, meetingThatJustEndedRoom) 

            # If theres a free room use it
            if len(freeRooms) > 0:
                curRoom = heapq.heappop(freeRooms)
                heapq.heappush(roomEndHeap, (meetingEndTime, curRoom))
                retRoomMeetingsCounter[curRoom] += 1
            else:
                nextMeetingToEnd = heapq.heappop(roomEndHeap)
                nextMeetingToEndTime = nextMeetingToEnd[0]
                nextMeetingToEndRom = nextMeetingToEnd[1]
                updatedMeetingEndTime = (nextMeetingToEndTime - meetingStartTime) + meetingEndTime
                heapq.heappush(roomEndHeap,(updatedMeetingEndTime, nextMeetingToEndRom))
                retRoomMeetingsCounter[nextMeetingToEndRom] += 1

        roomWithMostMeeting = (float('-inf'), None)
        # post processing 
        for key in retRoomMeetingsCounter:
            if retRoomMeetingsCounter[key] > roomWithMostMeeting[0]:
                roomWithMostMeeting = (retRoomMeetingsCounter[key], key)

        print(retRoomMeetingsCounter)
        print(roomWithMostMeeting)

        return roomWithMostMeeting[1]
    

sol = Solution()
# sol.mostBooked(2, [[0,10],[1,5],[2,7],[3,4]])
# sol.mostBooked(2, [[0,10],[1,2],[12,14],[13,15]])
# sol.mostBooked(4, [[33,42],[31,44],[40,48],[35,42],[21,22],[44,46],[29,32]])
sol.mostBooked(2, [[43,44],[34,36],[11,47],[1,8],[30,33],[45,48],[23,41],[29,30]])