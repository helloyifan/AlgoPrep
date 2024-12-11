# Notes both DFS and BFS have O(matrix) runtime, however, 
# DFS will explore unnecssary branches even after finding result, 
# BFS Stops immediately when the shortest path is found
from typing import List
from collections import deque
class Solution:
    # DFS Solution
    # TC: O(matrix) beucase we wont explore deeper with visited() mechanism, matrix is the size of the grid (lxl)
    # SC: O(matrix) because eacj cell gets added to grid and queue and potentially added to heap
    def dfs_shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        maxDim  = len(grid)-1
        dirs = [[1,0], [1,1], [0,1], [-1,0], [-1,-1], [0,-1], [-1, 1], [1,-1]]
        visited = set()

        def dfs(grid, node, dirs, visited):
            if node in visited:
                return -1
            if node[0] < 0 or node[0] > maxDim:
                return -1
            if node[1] < 0 or node[1] > maxDim:
                return -1
            if grid[node[0]][node[1]] == 1:
                return -1
            
            # This is when we finish
            if node == (maxDim, maxDim):
                return 1
            
            visited.add(node)

            shortestPath = float('inf')
            for d in dirs:
                nextSpot = (node[0]+d[0], node[1]+d[1])
                cur = dfs(grid, nextSpot, dirs, visited)
                if cur >= 0:
                    shortestPath = min(shortestPath, cur)
            
            # BAD ME: WHEN BACKTACKING ALWAYS CLEAN UP VISITED
            visited.remove(node)
            
            if shortestPath == float('inf'):
                return -1

            return shortestPath+1
        
        ret = dfs(grid, (0,0), dirs, visited)
        print(ret)
        return ret
    
    # O(matrix) we explore every cell
    # O(matrix) every cell could be in visited, every cell could be on stack
    def bfs_shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        maxDim = len(grid)-1
        s = deque()
        s.append((0,0))
        dirs = [[1,0], [1,1], [0,1], [-1,0], [-1,-1], [0,-1], [-1, 1], [1,-1]]
        doneFlag = False
        step = 0
        visited = set()
        while len(s) > 0:
            if doneFlag == True:
                break
            step += 1
            tempS = deque([])
            while len(s) > 0:
                spot = s.popleft()
                if spot[0] < 0 or spot[0] > maxDim:
                    continue
                if spot[1] < 0  or spot[1] > maxDim:
                    continue
                
                if grid[spot[0]][spot[1]] == 1:
                    continue
                
                if spot in visited:
                    continue
                
                if spot[0] == maxDim and spot[1] == maxDim:
                    doneFlag = True
                    break
                visited.add(spot)


                for d in dirs:
                    tempS.append((spot[0]+d[0], spot[1]+d[1]))
            s = tempS
        
        if doneFlag == False:
            step = -1

        print(step)
        return step


sol = Solution()
sol.bfs_shortestPathBinaryMatrix([[0,1],[1,0]])
sol.bfs_shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]])
sol.bfs_shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,1]]) #-1
#sol.shortestPathBinaryMatrix([[0,0,0],[0,1,0],[0,0,0]])

# [0,0,0],
# [0,1,0],
# [0,0,0]