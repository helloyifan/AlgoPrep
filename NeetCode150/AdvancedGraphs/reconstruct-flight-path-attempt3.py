import copy
from typing import List
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList = defaultdict(list)
        for ticket in tickets:
            adjList[ticket[0]].append(ticket[1])
        
        for key in adjList:
            adjList[key].sort()

        print(adjList)
        def dfs(node, ret):
            if not node in adjList:
                return
            
            children = adjList[node]
            for c in children:
                dfs(c)





sol = Solution()
# All of the tickets belong to someone who originally departed from "JFK". 
# Your objective is to reconstruct the flight path that this person took, assuming each ticket 
# was used exactly once.

sol.findItinerary([["BUF","HOU"],["HOU","SEA"],["JFK","BUF"]]) # ["JFK","BUF","HOU","SEA"]
# sol.findItinerary([["HOU","JFK"],["SEA","JFK"],["JFK","SEA"],["JFK","HOU"]]) #["JFK","HOU","JFK","SEA","JFK"]
# sol.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]) #["JFK","NRT","JFK","KUL"]
# sol.findItinerary([["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]])
