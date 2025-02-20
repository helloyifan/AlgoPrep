# Notes:
# Simple logic:
# If some interval overlaps any interval (for any employee), then it won't be included in the answer. 
# So we could reduce our problem to the following: 
# given a set of intervals, find all places where there are no intervals.


# TC: O(nlogn) where n is number of event
# SC: O(n)

# There is also a heap solution https://leetcode.com/problems/employee-free-time/editorial/


# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]': # type: ignore 

        listOfAllIntervals = []
        for s in schedule:
            listOfAllIntervals.extend(s)

        # Step 2.
        # Merge interval algorithm
        # first sort

        listOfAllIntervals.sort(key=lambda x: x.start)

        # then  iterate and merge and hold onto temp
        mergedIntervals = []
        tempInterval = None
        for interval in listOfAllIntervals:
            # base case
            if tempInterval == None:
                tempInterval = interval
            else:
                if tempInterval.end >= interval.start:
                    if tempInterval.end < interval.end:
                        tempInterval.end = interval.end
                    # otherwise we do need to chagne tempInterval, it starts before and ends after
                else:
                    mergedIntervals.append(tempInterval)
                    tempInterval = interval
        
        # Add the last interval to the list
        mergedIntervals.append(tempInterval)


        # Step 3. Find the inverse (times where people are free)
        tempStartTime = None
        freeTimeIntervals = []
        for i in mergedIntervals:
            # base case = 
            if tempStartTime == None:
                tempStartTime = i.end
            else:
                freeTimeForEveryone = Interval(tempStartTime, i.start)
                freeTimeIntervals.append(freeTimeForEveryone)
                tempStartTime = i.end

        # Print ret 
        for i in freeTimeIntervals:
            print(i.start, i.end)
        print('---')
        return freeTimeIntervals
    
sol = Solution()
# sol.employeeFreeTime([[[1,2],[5,6]],[[1,3]],[[4,10]]]) # [[3,4]]
sol.employeeFreeTime(
    [
        [Interval(1,2),Interval(5,6)],
        [Interval(1,3)],
        [Interval(4,10)]
    ]
)
# sol.employeeFreeTime([[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]) # [[5,6],[7,9]]
sol.employeeFreeTime(
    [
        [Interval(1,3),Interval(6,7)],
        [Interval(2,4)],
        [Interval(2,5), Interval(9,12)]
    ]
)