from typing import List
 
# Spent 15 mins almost solved
# just need to count how many times key  in adjList without collision with visited
    # - if theres collision with visited we bail out asap
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adjList = {}
        for i in range(n):
            adjList[n] = None

        for e in edges:
            adjList[e[0]] = e[1]

        def dfs(node, curVisited, visited):
            if node == None:
                return 
            
            if node in curVisited:
                return 

            curVisited.append(node)
            if node not in adjList:
                return
            ret = dfs(adjList[node], curVisited, visited)
            return 


        print(adjList)
        ret = 0
        visited = {}

        for key in adjList:
            tempCurVisited = []
            dfs(key, tempCurVisited, visited)
            print(tempCurVisited)
        
        return

sol = Solution()
#sol.countComponents(3, [[0,1], [0,2]])
sol.countComponents(6, [[0,1], [1,2], [2,3], [4,5]])