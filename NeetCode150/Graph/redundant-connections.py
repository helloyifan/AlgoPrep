# Attempt 1. Tried for 30mins, used DFS and cycle detection
  # - I does most of what hte question asks, but it doesn return the last edge from the input, it just returns the last edge found via dfs
# Attempt 1. Time complexity: O(n) because we explore every edge, Space Complexity: O(n) because we make the adjacency matrix


from collections import defaultdict
from typing import List
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
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

sol = Solution()
#sol.findRedundantConnection([[1,2],[1,3],[3,4],[2,4]]) #[2,4]
sol.findRedundantConnection([[1,2],[1,3],[1,4],[3,4],[4,5]]) #[3,4]