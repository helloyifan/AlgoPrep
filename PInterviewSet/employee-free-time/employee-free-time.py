from typing import List

# Notes: There is also a heap solution thats faster but i think this works fine

# TC: O(nlogn) where n is number of event
# SC: O(n)

# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]': # type: ignore

        # Step 1. Flatten this list of lists to be a single list
        events = []
        for employee in schedule:
            for event in employee:
                events.append(event)
        
        # Step 2. Sort list by start time (so we can merge internvals)
        events.sort(key= lambda x: x.start) # O(nlogn) where n is number of event

        # Step3. Merge internval O(n)
        # merge interval algorithm
        mergedEvents = []
        cur = None #hold one event and edit its end time

        for i in range(len(events)):
            if cur == None:
                cur = events[i] # hold the first event
                continue

            next = events[i]
            if cur.end >= next.start:
                if cur.end < next.end:
                    cur.end = next.end
            else: # cur.end < next.start
                mergedEvents.append(cur)
                cur = next

        mergedEvents.append(cur)

        employeeBreaks = []
        # Step 4. post process mergedEvents to find gaps
        for i in range(len(mergedEvents)-1):
            cur = mergedEvents[i]
            next = mergedEvents[i+1]
            employeeBreaks.append(Interval(cur.end, next.start))

        print(employeeBreaks)
        return employeeBreaks

sol = Solution()
sol.employeeFreeTime(
    [
        [Interval(1,2),Interval(5,6)],
        [Interval(1,3)],
        [Interval(4,10)]
    ]
)
