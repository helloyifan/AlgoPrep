from typing import List
from collections import defaultdict

class Solution:
    # Top down neetcode approach
    # This solution is too slow btw
    # TC: Since we are potentially back tracking on every Edge, the TC is O(E^2)
    # SC: Since we are storing every edge, the S is O(E)
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Step 1. Make graph
        dd = defaultdict(list)
        
        # Step 1.5. Make sure the tickets are sorted in reverse order by start airport
        tickets.sort()
        for t in tickets:
            dd[t[0]].append(t[1])

        # Step 2. More top down dfs, where we try to add the cur airport
        # to ret, until it doesnt work, 
        # if we aren't able to add it, 
            # we pop it from our itenary and try the next
            # We also add back the airport to the default dict

        itenary = ['JFK']
        def dfs(airport, dd):
            if len(itenary) == len(tickets)+1:
                return True

            if not airport in dd:
                return False
            
            temp = list(dd[airport]) # best to not modify an object while we iterate on it
            for indexOfNextAirport, nextAirport in enumerate(temp):
                itenary.append(nextAirport)
                dd[airport].pop(indexOfNextAirport)
                
                if dfs(nextAirport, dd):
                    return True
                # Back track cleanup
                itenary.pop()
                dd[airport].insert(indexOfNextAirport, nextAirport)
        
        # Step 3. kick start
        dfs('JFK', dd)
        return itenary
    
    # Passes leetcode
    # TC: Sorting makes this O(ElogE) since every ticket is an edge

    # SC: O(E) since we are storing every Edge
    # def backWardsFindItinerary(self, tickets: List[List[str]]) -> List[str]:
    #     # Step 1. Make graph
    #     dd = defaultdict(list)
        
    #     # Step 1.5. Make sure the tickets are sorted in reverse order by start airport
    #     tickets.sort(reverse=True)
    #     for t in tickets:
    #         dd[t[0]].append(t[1])

    #     itenary  = []
    #     # Step 2. DFS
    #     def dfs(airport, dd):
    #         while dd[airport]:
    #             nextAirport = dd[airport].pop() # Pop ticket that you have taken
    #             dfs(nextAirport, dd)
    #         # Once we reach an airport with no outgoing edges, or in other words, no more destinations to visit, we start backtracking.
    #         # Importantly, we are essentially building the itinerary in reverse during this phase because of the way DFS works.
    #         # As we backtrack, we are popping from the call stack, revisiting the airports in the reverse order of how they will eventually appear in the itinerary.
    #         itenary.append(airport)

    #         return
    #     # Step 3. Kick start the dfs
    #     dfs('JFK', dd)
    #     # Step 4. Reverse the itenary
    #     return itenary[::-1]
    

            
sol = Solution()
#print(sol.findItinerary( [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
#print(sol.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))

# print(sol.findItinerary([["JFK","AAA"],["BBB","JFK"],["JFK","BBB"]]))


print(sol.altFindIntineary( [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
print(sol.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
