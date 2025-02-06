
# TC: BFS: Edge is bus route, Vertex is stop. Since we are visited every edge and vertex in wrost case O(V*E)
# SC: queue could potentially hold every stop so O(vertex), however DD stops all routes and stops so O(V+E)
from typing import List
from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        stopToBusRoute = defaultdict(list)

        for busRouteIdx, busRoute in enumerate(routes):
            for stop in busRoute:
                stopToBusRoute[stop].append(busRouteIdx)
        print(stopToBusRoute)

        # Use BFS to find the busRoute that covers target stop
        q = deque()

        visitedBusRoute = set()
        visitedStop = set()


        for e in stopToBusRoute[source]:
            q.append(e)
        
        busRideCounter = 0

        while len(q) > 0:
            tempQ = deque()
            busRideCounter += 1
            while len(q) > 0:
                curBusRouteIdx = q.popleft()

                if curBusRouteIdx in visitedBusRoute:
                    continue

                visitedBusRoute.add(curBusRouteIdx)

                curBusRoute = routes[curBusRouteIdx]
                
                if target in curBusRoute:
                    return busRideCounter
                
                for stop in curBusRoute:
                    if stop in visitedStop:
                        continue
                    visitedStop.add(stop)
                    for e in stopToBusRoute[stop]:
                        tempQ.append(e)   
            q = tempQ

        return -1
    
sol = Solution()
print(sol.numBusesToDestination( [[1,2,7],[3,6,7]], 1, 6)) # 2
# print(sol.numBusesToDestination( [[7,12],[4,5,15],[6],[15,19],[9,12,13]], 15, 12))# -1 
print(sol.numBusesToDestination([[1,7],[3,5]], 5, 5)) # 0