# Attempt 1. Tried for 30mins, used DFS and cycle detection
  # - I does most of what hte question asks, but it doesn return the last edge from the input, it just returns the last edge found via dfs
# Attempt 1. Time complexity: O(n) because we explore every edge, Space Complexity: O(n) because we make the adjacency matrix
# Attempt 2. Spent anothter 15mins didnt getit, basically new idea is to do DFS each time we add an edge
# But whats the starting node for our DFS?, am i doing DFS wrong?
# Attempt 3. Took 10 mins, basically same as attempt 2but made DFS bi directional

from collections import defaultdict
from typing import List
class Solution:
    # attempt 1 with a one time DFS solution. I think its possible but not going to try any more
    def attempt1(self, edges: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        for e in edges:
            adjList[e[0]].append(e[1])
        print(adjList)

        # step 1 cycle detection
        def dfsCycleDetection(curNode, prevNode, visited, prevEdge):
            if curNode in visited:
                prevEdge[0] = curNode
                prevEdge[1] = prevNode

                return True
            

            visited.append(curNode)
            childNodes = adjList[curNode]
            for node in childNodes:
                t = dfsCycleDetection(node, curNode, visited, prevEdge)
                if t == True:
                    return True
            return False
        
        
        startNode = next(iter(adjList)) #just the first thing in the list, bcuz its a connected graph
        visited = []
        prevEdge = [-1, -1]
        cycleFound = dfsCycleDetection(startNode, -1 , visited, prevEdge)

        if cycleFound:
            ret = prevEdge
        else:
            ret = [-1, -1] # no cycles found
        print(visited)
        print(prevEdge)
        return prevEdge
    
    def attempt2(self, edges: List[List[int]]) -> List[int]:
        def dfsCycleDetection(adjList, curNode, visited):
            #print(adjList, curNode, visited)
            if curNode in visited:
                return True
            
            visited.append(curNode)
            childNodes = adjList[curNode]
            for node in childNodes:
                t = dfsCycleDetection(adjList, node, visited)
                if t == True:
                    return True
            return False
        
        adjList = defaultdict(list)
        startNode = edges[0][0]

        for e in edges:
            adjList[e[0]].append(e[1])
            
            # First time setup, i think we can always use the first node

            cycleExist = dfsCycleDetection(adjList, startNode, [])
            if cycleExist:
                print(e)
                return e

        # if we never found the cycle
        print("not found")
        return [-1, -1]
    
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        def dfsCycleDetection(adjList, curNode, prev, visited):
            if curNode in visited:
                return True
            
            visited.append(curNode)
            childNodes = adjList[curNode]
            for c in childNodes:
                if c != prev:
                    t = dfsCycleDetection(adjList, c, curNode, visited)
                    if t == True:
                        return True
                    
            return False

        adjList = defaultdict(list)
        for e in edges:
            startNode = e[0]
            endNode = e[1]
            adjList[startNode].append(endNode)
            adjList[endNode].append(startNode)
            
            cycleExist = dfsCycleDetection(adjList, startNode, -1 , [])
            if cycleExist:
                print(e)
                return e
        print("not found")
        return [-1, -1]    

sol = Solution()
sol.findRedundantConnection([[1,2],[1,3],[3,4],[2,4]]) #[2,4]
sol.findRedundantConnection([[1,2],[1,3],[1,4],[3,4],[4,5]]) #[3,4]
sol.findRedundantConnection([[3,4],[1,2],[2,4],[3,5],[2,5]])