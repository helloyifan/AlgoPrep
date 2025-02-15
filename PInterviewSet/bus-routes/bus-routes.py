from typing import List
from collections import defaultdict
from collections import deque

# Notes: 
# We have relationship between routes to stop
# build relationship between stop to routes (routes == bus)
# Dont go to the same stop
# Dont go to the same route
# Only routes go onto q
    # Iterate through every stop
        # For each stop add every route that it can go to

# TC: Worst case we visit all stops and route O(n*m)
# SC: stop to routes is O(n*m), visited  set is O(n+m), q is O(n)

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        stop_to_routes = defaultdict(set)
        
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].add(i)
        print(stop_to_routes)

        # Step 2: BFS to find shortest route path
        q = deque()
        visited_routes = set()
        visited_stops = set()
        transfers = 0

        # Add all bus routes that contain the source
        # Initalized q with all routes that source is in
        for route in stop_to_routes[source]:
            q.append(route)
            visited_routes.add(route)

        print(q)

        # Step 3 bfs
        while len(q) > 0:
            transfers += 1
            tempQ = deque()
            
            while len(q)> 0:
                cur_route = q.pop()

                for stop in routes[cur_route]:
                    if stop == target:
                        return transfers
                
                    if not stop in visited_stops:
                        visited_stops.add(stop) # visited manage

                        for next_route in stop_to_routes[stop]:
                            # Check all routes that go through this stop
                            if not next_route in visited_routes:
                                visited_routes.add(next_route) # visited manage
                                tempQ.append(next_route)

            q = tempQ
        
        return -1
    

sol = Solution()
print(sol.numBusesToDestination([[1,2,7],[3,6,7]], 1, 6))
print(sol.numBusesToDestination([[7,12],[4,5,15],[6],[15,19],[9,12,13]], 15, 12))
