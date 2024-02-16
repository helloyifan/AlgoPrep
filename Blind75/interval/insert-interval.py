# Took 34min,
# For interval problem its important that intervals are sorted
# note, we only write the merged interval to the ret once we know it cant be merged any longer
# I think the conditional could be simplified but im shits for brains

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        finalIndexHandled = None

        for i, curInterval in enumerate(intervals):
            if newInterval[1] < curInterval[0]:
                ret.append(newInterval)
                finalIndexHandled = i
                break

            # case 1 (merge based on first val in pair)
            # case 2 (merge based on second val in pair)
            # case 3 (merge when it's totally encapsulated)
            if (newInterval[0] <= curInterval[0] and newInterval[1] >= curInterval[0]) or \
                (newInterval[0] <= curInterval[1] and newInterval[1] >= curInterval[1]) or \
                (newInterval[0] >= curInterval[0] and newInterval[1] <= curInterval[1]):
                    # if its valid for merge then merge, for cond3 is just a replace lol, 
                    newInterval[0] = min(curInterval[0], newInterval[0])
                    newInterval[1] = max(curInterval[1], newInterval[1])
                # if it doesn't fall into any case
            else:
                ret.append(curInterval)

    
        if finalIndexHandled != None:
            ret.extend(intervals[finalIndexHandled:])
        else: # handle the ([], [5,7]) case
            ret.append(newInterval)
        return ret

if __name__ == '__main__':
    s = Solution()
    # print(s.insert([[1,3],[6,9]], [2,5]))
    # print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
    print(s.insert([[1,5]], [2,3]))