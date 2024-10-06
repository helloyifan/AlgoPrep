# spent 31 min a wip
# spent another 50 min on attempt1, i think its a valid backtracking way with some weird code, maybe works but takes too lopng

# Attempt 2 tried for 34 mins didnt solve it
import copy
from typing import List
from collections import defaultdict
class Solution:
    def attempt1 (self, tickets: List[List[str]]) -> List[str]:
        adjList = defaultdict(list)

        for t in tickets:
            start = t[0]
            destination = t[1]
            adjList[start].append(destination)
        
        for key in adjList:
            adjList[key].sort()

        #print(adjList)

        def dfs(cur, ret, visited):

            ret.append(cur)
            visited.append(cur)

            childNodes = adjList[cur]
            while len(childNodes) > 0:
                c = childNodes[0]
                # We only want to remove C if its the right next step
                # So we might add it back later
                if c in adjList[cur]:
                    adjList[cur].remove(c)

                curRet = copy.copy(ret)
                dfs(c, curRet, visited)
                
                # Might infinite loop
                if not self.isAdjListEmpty(adjList):
                    # print(curRet, adjList)
                    adjList[cur].append(c)
                else:
                    self.dumbCopy(ret, curRet)

            return

        ret = []
        dfs('JFK', ret, [])
        print(ret)
        return ret
    
    def isAdjListEmpty(self, adjList):
        #print("check: ", adjList)

        for k in adjList:
            if len(adjList[k]) > 0:
                return False
        return True
    
    def dumbCopy (self, oldL, newL):
        while len(oldL) > 0:
            oldL.pop()
        for i in newL:
            oldL.append(i)
    
    def attemp2(self, tickets: List[List[str]]) -> List[str]:
        adjList = defaultdict(list)

        for t in tickets:
            start = t[0]
            destination = t[1]
            adjList[start].append(destination)
        
        for key in adjList:
            adjList[key].sort()

        tempAdjList = defaultdict(list)

        def dfs(cur, ret):
            tempRet = copy.copy(ret)
            tempRet.append(cur)

            # base case
            if len(adjList[cur]) == 0:
                return tempRet

            while len(adjList[cur]) > 0:
                c = adjList[cur][0]
                print(cur, c, adjList)
                adjList[cur].remove(c)
                curRet = dfs(c, tempRet)
                if self.isAdjListEmpty(adjList):
                    return curRet
                else:
                    tempAdjList[cur].append(c)

            raise Exception(f"We are saying that theres no possible way atm: {cur}", )

        ret = []
        while not self.isAdjListEmpty(adjList):
            print(adjList)
            ret = dfs("JFK", ret)
            adjList = tempAdjList
            tempAdjList = defaultdict(list)
            
        print(ret)
        return(ret)
    
    # Attempt3
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList = defaultdict(list)

        for t in tickets:
            start = t[0]
            destination = t[1]
            adjList[start].append(destination)
        
        for key in adjList:
            adjList[key].sort()

        def dfs(cur, ret):
            if cur in adjList:
                destinations = copy.copy(adjList[cur])
                while destinations:
                    dest = destinations[0]
                    adjList[cur].pop(0)
                    dfs(dest, ret)
                    destinations = copy.copy(adjList[cur])

                ret.append(cur)
        ret = []
        dfs("JFK", ret)
        ret.reverse()

        print(ret)
        return ret

sol = Solution()
# All of the tickets belong to someone who originally departed from "JFK". 
# Your objective is to reconstruct the flight path that this person took, assuming each ticket 
# was used exactly once.

sol.findItinerary([["BUF","HOU"],["HOU","SEA"],["JFK","BUF"]]) # ["JFK","BUF","HOU","SEA"]
# sol.findItinerary([["HOU","JFK"],["SEA","JFK"],["JFK","SEA"],["JFK","HOU"]]) #["JFK","HOU","JFK","SEA","JFK"]
# sol.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]) #["JFK","NRT","JFK","KUL"]
# sol.findItinerary([["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]])
