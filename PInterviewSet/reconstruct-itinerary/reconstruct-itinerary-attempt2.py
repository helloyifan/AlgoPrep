#itinerary

from typing import List
from collections import defaultdict

class Solution:
    def backwardsFindItinerary(self, tickets: List[List[str]]) -> List[str]:
        dd = defaultdict(list)

        tickets.sort(reverse=True)
        for t in tickets:
            dd[t[0]].append(t[1])

        itinerary = []
        def dfs(loc, dd):
            while dd[loc]:
                nextSpot = dd[loc].pop()
                dfs(nextSpot, dd)
            itinerary.append(loc)
        
        dfs('JFK', dd)
        return itinerary[::-1]

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dd = defaultdict(list)

        tickets.sort()
        for t in tickets:
            dd[t[0]].append(t[1])
        
        itinerary = ['JFK'] # Initalize with JFK
        def dfs(loc, dd):
            if len(itinerary) == len(tickets)+1:
                return True # we found a path
            if len(dd[loc]) == 0:
                return False
            
            tempList = dd[loc]
            for i, e in enumerate(tempList):
                nextLoc = dd[loc].pop(i)
                itinerary.append(nextLoc)

                ret = dfs(nextLoc, dd)
                if ret == True:
                    return True # we found a path, push it up

                # Backtrack cleanup
                itinerary.pop()
                dd[loc].insert(i, e)
        
        dfs('JFK', dd)
        return itinerary

sol = Solution()
#print(sol.findItinerary( [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
#print(sol.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
print(sol.findItinerary([["JFK","AAA"],["BBB","JFK"],["JFK","BBB"]]))