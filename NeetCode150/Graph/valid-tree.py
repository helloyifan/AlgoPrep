# Solved in 10 mins from intuition
# Kinda looked at the answer 
# leveraged adjaceny lists, and the fact that in this question, edges are bi directional in idea,
# but represented as uni-directional (smallNode -> largeNode)
from typing import List
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {}
        for i in range(n):
            adjList[i] = []

        for e in edges:
            adjList[e[0]].append(e[1])
        print(adjList)

        visited = set()

        def dfs(node):
            if node in visited:
                return False
            
            visited.add(node)

            curList = adjList[node]
            for nextNode in curList:
                curRet = dfs(nextNode)

                if curRet == False:
                    return False
            
            return True

        ret = dfs(0)
        print(ret)
        return ret
sol = Solution()
sol.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) # True
sol.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) # False
