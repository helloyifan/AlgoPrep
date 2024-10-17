# tried again solved in 25 mins
# The super hint is only adding whats needed to the heap when applicible
# Runtime complexity:
# Adjlist building O(n^2)
# While loop O(n * logN) for doing n heap pop
#  While and for loop  O(n^2*logN) for doing n*n heap pushs
from typing import List
from collections import defaultdict
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #adjList = [[0 for i in range(len(points))]for i in range(len(points))]
        
        adjList = defaultdict(list)
        # Setup adj list
        for fromI, frompoint in enumerate(points):
            for toI, topoint in enumerate(points):
                manV = self.manhattenCalcuation(frompoint, topoint)
                adjList[tuple(frompoint)].append(manV)

        #print(adjList)

        #try shit
        startingPoint = (points[0][0], points[0][1])
        startingTuple = (0 , startingPoint)
        h = [startingTuple]
        heapq.heapify(h)

        ret = 0
        visited = set()
        while len(visited) < len(points):
            curHeapVal = heapq.heappop(h)
            curWeight = curHeapVal[0]
            curNodeTuple = curHeapVal[1]
            curNeighbors = adjList[curNodeTuple]

            if not curNodeTuple in visited:
                visited.add(curNodeTuple)
                ret += curWeight
            
            for neighborIndex, neighborVal in enumerate(curNeighbors):
                newPoint = tuple(points[neighborIndex])
                if neighborVal != 0: #not sure if this is the best way to prevent adding urself
                    heapq.heappush(h, (neighborVal, newPoint))
            del adjList[curNodeTuple] #once the values are all added, remove it from adjlist, its already considered


        print(ret)
        return ret
    
    def manhattenCalcuation(self, f, t):
        return abs(f[0] - t[0]) + abs(f[1] - t[1])

sol = Solution()
#sol.minCostConnectPoints([[0,0],[2,2],[3,3],[2,4],[4,2]])
sol.minCostConnectPoints([[0,0]])

#sol.minCostConnectPoints([[2,-3],[-17,-8],[13,8],[-17,-15]]) # should be 53