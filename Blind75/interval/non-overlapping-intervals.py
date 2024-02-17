class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals = sorted(intervals, key= lambda x: x[0])
        print(intervals)
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        ret = 0
        curIntervalEnd = None

        for interval in intervals:
            # Set curIntervalEnd as its determine the min interval thats possible atm
            # Min interval means min overlap
            # Big interval is like if you have [1-10] and [1,2], [2,3], [3,4] then theres so many overlap
            if (curIntervalEnd == None or #  Base case
                curIntervalEnd <= interval[0]): # [0,1] to [2,3] does not overlap and [1,2] to [2,3] do not overlap either
                
                curIntervalEnd = interval[1]
            else:
                ret += 1
                curIntervalEnd = min(curIntervalEnd, interval[1])
        return ret

if __name__ == '__main__':
    s = Solution()
    print(s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))