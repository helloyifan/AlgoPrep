# Notes: Sort
# temporarily hold on to the interval you are working on, add to list after ur done
# Careful handling of if conditions
# TC: O(nlogn) for initial sorting, O(n) for main loop logic
# SC: O(n) for building out result
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort() # O(nlogn)
        
        ret = [] #O(n)
        curInterval = None

        for i in range(len(intervals)): #O(n)
            iterateInterval = intervals[i]
            # Initalize
            if curInterval == None:
                curInterval = iterateInterval 
            else:
                if curInterval[1] >= iterateInterval[0]:
                    if curInterval[1] < iterateInterval[1]:
                        curInterval[1] = iterateInterval[1]
                    else:
                        # This is when curInterval is bigger than both H,T and iterateInterval
                        pass
                else:
                    ret.append(curInterval)
                    curInterval = iterateInterval
        
        ret.append(curInterval)
        
        print(ret)
        return ret
         

    
sol = Solution()
sol.merge([[1,3],[2,6],[8,10],[15,18]])