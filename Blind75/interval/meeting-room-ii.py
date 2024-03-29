# Had to do it on neetcode website instead of leetcode
# One thing i dont really see is why we need to sort by key.end rather then key.start
# Took 20 mins
"""
Definition of Interval:
"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals):
        if len(intervals) == 0:
            return 0 # Phuck you stupid edge case 
        
        intervals = sorted(intervals, key = lambda key: key.end)
        # We use key.end because we wanna evaluate the meetings with late end times last
        # That way we can figure out if fit into any other days

        lastMeetingEndTimes = []
        lastMeetingEndTimes.append(intervals[0].end)
        for i, interval in enumerate(intervals[1:]):
            
            swapPos = None
            for j, endTime in enumerate(lastMeetingEndTimes):
                if endTime <= interval.start:
                    swapPos = j
                    break
            
            if swapPos != None:
                lastMeetingEndTimes[swapPos] = interval.end
            else: # if we couldnt find any time in the current days, then add a new entry
                lastMeetingEndTimes.append(interval.end)


        dayCounter = len(lastMeetingEndTimes)
        
        return dayCounter

if __name__ == '__main__':
    s = Solution()
    # print(s.minMeetingRooms([
    #     Interval(0, 40),
    #     Interval(5, 10),
    #     Interval(15, 20),
    # ]))

    # print(s.minMeetingRooms([
    #     Interval(4, 9)
    # ]))

    print(s.minMeetingRooms([
        Interval(1, 5),
        Interval(2, 6),
        Interval(3, 7),
        Interval(4, 8),
        Interval(5, 9),
    ]))