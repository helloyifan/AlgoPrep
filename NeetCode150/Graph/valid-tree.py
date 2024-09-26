# Solved in 10 mins from intuition
# Spend another 15 min thinnking more about it and got it 
# Basically have to make the imrpovement of adding both diferects to adjaceny list
# and prevent the node from going back to the prev node
from typing import List
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {}
        for i in range(n):
            adjList[i] = []

        for e in edges:
            adjList[e[0]].append(e[1])
            adjList[e[1]].append(e[0])
            
        print(adjList)

        visited = set()

        def dfs(node, prevNode):
            if node in visited:
                return False
            
            visited.add(node)

            curList = adjList[node]
            for nextNode in curList:
                if nextNode != prevNode:
                    curRet = dfs(nextNode, node)

                    if curRet == False:
                        return False
            
            return True

        ret = dfs(0, -1)
        if len(visited) != n:
            ret = False

        print(ret)
        return ret
    
sol = Solution()
sol.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) # True
sol.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) # False
sol.validTree(5, [[0, 1], [2, 1], [3, 2], [3, 1], [4, 1]]) # False
sol.validTree(4, [[0, 1], [2, 3]]) # False
sol.validTree(5, [[0, 1], [1, 3], [3, 2], [1, 4]]) # True
sol.validTree(5, [[0, 1], [2, 0], [3, 0], [1, 4]]) # True