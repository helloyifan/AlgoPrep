# spent 50 mins on this question, didnt get it 
# not exactly the right idea, i think dont we should populate the heap this way
# Runtime Complexity: 
# heap stuff is O(logN)
# Building heap is O(log n) * n * n so O(N^2logN) 
# REmoving from heap is O(nLogN) because we are just poping from heap N times
# So runtime is O(N^2logN) 
# Space complexity is O(n^2) since we are storing edges and theres n edges

from typing import List
from collections import defaultdict
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        h = []

        for fromPoint in points:
            for toPoint in points:
                if fromPoint != toPoint: # no point on having current location in imo,
                    tFrom = tuple(fromPoint)
                    tTo = tuple(toPoint)
                    mval = self.manhattenCalcuation(fromPoint, toPoint)
                    print("input:", (mval, tFrom, tTo))
                    heapq.heappush(h, (mval, tFrom, tTo))

        print('----')
        uniqueSet = set()
        ret = 0
        while len(h) > 0 and len(uniqueSet) < len(points):
            c = heapq.heappop(h)
            if len(uniqueSet) == 0:
                uniqueSet.add(c[1])

            if (not c[2] in uniqueSet):
                print("output: ", c)
                ret += c[0]
                uniqueSet.add(c[2])
        print(ret)
        return ret
    
    def manhattenCalcuation(self, f, t):
        return abs(f[0] - t[0]) + abs(f[1] - t[1])

sol = Solution()
sol.minCostConnectPoints([[0,0],[2,2],[3,3],[2,4],[4,2]])
sol.minCostConnectPoints([[0,0]])
sol.minCostConnectPoints([[2,-3],[-17,-8],[13,8],[-17,-15]]) # should be 53