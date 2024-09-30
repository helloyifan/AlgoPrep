from typing import List
 
# Spent 15 mins almost solved
# just need to count how many times key  in adjList without collision with visited
    # - if theres collision with visited we bail out asap

# Spent another 11 mins, solved it

# Time complexity:  O(a * log(a))
# Space complexity: O(a)

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adjList = {}
        for i in range(n):
            adjList[i] = []

        for e in edges:
            adjList[e[0]].append(e[1])

        print(adjList)
        def dfs(node, curVisited, ):
            if node == None:
                return 
            
            if node in curVisited:
                return 

            curVisited.append(node)
            if not node in adjList:
                return
            
            for childNode in adjList[node]:
                dfs(childNode, curVisited)
            return 


        #print(adjList)
        ret = 0
        visited = {}

        for key in adjList:
            tempCurVisited = []
            dfs(key, tempCurVisited)
            
            # Debugging
            print(tempCurVisited)

            # Post processing after DFS
            attachedToSomethingExisting = False
            for v in tempCurVisited:
                if not v in visited:
                    visited[v] = True
                else:
                    attachedToSomethingExisting = True
            
            if not attachedToSomethingExisting:
                ret += 1

        print(ret)
        return ret

sol = Solution()
sol.countComponents(3, [[0,1], [0,2]]) # 1
sol.countComponents(6, [[0,1], [1,2], [2,3], [4,5]]) # 3 
sol.countComponents(1, []) # 1