# Spent an hour on it, need to debug ret vs curRet
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
            print(ret)
            if (not node in adjList) or (len(adjList[node]) == 0):
                if self.adjListEmpty(adjList):
                    return (True, ret)
                else:
                    return (False, ret)
                
            children = adjList[node]
            failedChildrenCounter = 0 
            while len(children) > 0:
                if failedChildrenCounter == len(children):
                    return (False, ret)

                firstAlphaAirport = children.pop(0)
                ret.append(firstAlphaAirport)
                print(adjList)
                successOrFailure, curRet = dfs(firstAlphaAirport, ret)
                if successOrFailure == False:
                    #add back to list
                    children.append(firstAlphaAirport)
                    #remove from ret
                    curRet = curRet[:len(curRet)-1] #remove the last inserted
                    failedChildrenCounter +=1 # once every child has failed, this branch is doomed
                else:
                    return (True, curRet)
            

        ret = ["JFK"] # NOT SURE WHY RET IS WRONG
        success, actualRet = dfs("JFK", ret)
        print(actualRet)
        return actualRet
    
    def adjListEmpty(self, adjList):
        for key in adjList:
            if len(adjList[key]) > 0:
                return False
        return True

sol = Solution()
# All of the tickets belong to someone who originally departed from "JFK". 
# Your objective is to reconstruct the flight path that this person took, assuming each ticket 
# was used exactly once.

# sol.findItinerary([["BUF","HOU"],["HOU","SEA"],["JFK","BUF"]]) # ["JFK","BUF","HOU","SEA"]
# sol.findItinerary([["HOU","JFK"],["SEA","JFK"],["JFK","SEA"],["JFK","HOU"]]) #["JFK","HOU","JFK","SEA","JFK"]
sol.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]) #["JFK","NRT","JFK","KUL"]
# sol.findItinerary([["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]])
# sol.findItinerary([["JFK","AAA"],["AAA","JFK"],["JFK","BBB"],["JFK","CCC"],["CCC","JFK"]]) # ["JFK","AAA","JFK","CCC","JFK","BBB"]
