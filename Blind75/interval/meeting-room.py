# It took 12min because im a bit autistic, its a really easy problem
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals):
        intervals = sorted(intervals, key = lambda k: k[0])
        print(intervals)
        prevEnd = None
        for i in intervals:
            if prevEnd != None and i[0] < prevEnd:
                return False
            prevEnd = i[1]
            
        return  True

if __name__ == '__main__':
    s = Solution()
    print(s.canAttendMeetings([(0,30),(5,10),(15,20)]))
    # print(s.canAttendMeetings([(6, 10), (0,30),(5,10),(15,20)]))
    print(s.canAttendMeetings([(5,8),(9,15)]))
    print(s.canAttendMeetings([(0,15),(15,30),(30,45),(45,60),(60,75),(75,90),(85,100)]))
    print(s.canAttendMeetings([(1,2),(1,3)]))