# spent 31 min a wip

import copy
from typing import List
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList = defaultdict(list)

        for t in tickets:
            start = t[0]
            destination = t[1]
            adjList[start].append(destination)
        
        for key in adjList:
            adjList[key].sort()

        print(adjList)

        def dfs(cur, ret, visited):

            ret.append(cur)
            visited.append(cur)

            childNodes = adjList[cur]
            for c in childNodes:
                #print("adjList: ", adjList)
                if c in adjList[cur]:
                    adjList[cur].remove(c)
                #print('updated: ', adjList)
                #print('---')
                dfs(c, ret, visited)
            return
        

        ret = []
        dfs('JFK', ret, [])
        print(ret)
        return ret
    
sol = Solution()
# All of the tickets belong to someone who originally departed from "JFK". 
# Your objective is to reconstruct the flight path that this person took, assuming each ticket 
# was used exactly once.

sol.findItinerary([["BUF","HOU"],["HOU","SEA"],["JFK","BUF"]]) # ["JFK","BUF","HOU","SEA"]
sol.findItinerary([["HOU","JFK"],["SEA","JFK"],["JFK","SEA"],["JFK","HOU"]]) #["JFK","HOU","JFK","SEA","JFK"]
sol.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]) #["JFK","NRT","JFK","KUL"]
