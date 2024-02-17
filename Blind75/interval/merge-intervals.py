# Took 13 min, not too bad

class Solution(object):
    def merge(self, intervals):
        # For interval questions, it needs to be sorted
        intervals = sorted(intervals, key=lambda x: x[0])

        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        ret = []
        curInterval = None
        for interval in intervals:
            print(curInterval)
            if curInterval == None:
                curInterval = interval
            elif curInterval[1] < interval[0]:
                ret.append(curInterval)
                curInterval = interval
            else:
                curInterval[0] = min(curInterval[0], interval[0])
                curInterval[1] = max(curInterval[1], interval[1])
        # append whats left
        if curInterval != None:
            ret.append(curInterval)

        return ret

if __name__ == '__main__':
    s = Solution()
    print(s.merge([[1,3],[2,6],[8,10],[15,18]]))
    print(s.merge([[1,4],[4,5]]))
    print(s.merge([[1,4],[0,1]]))
    print(s.merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))