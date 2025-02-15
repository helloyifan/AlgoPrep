# Notes: Standard DFS with DP solution
# TC:O(2^(mn)):if at each step of a DFS traversal you have 2 options and the recursion depth is mn, without DP
# TC: O(2^(m+n)) if there is memoization, which im not sure if i believe tbh
# SC: O(m*n) since we have memoization(dp), visited is also (m+n)

from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        maxR = len(obstacleGrid) - 1
        maxC = len(obstacleGrid[0])- 1

        dp = {}

        def dfs(r, c, visited):
            if (r,c) in dp:
                return dp[(r,c)]

            if r < 0 or r >  maxR or c < 0 or c > maxC:
                return 0
            
            if obstacleGrid[r][c] == 1:
                return 0
            
            if (r,c) in visited:
                return 0

            if r == maxR and c == maxC:
                return 1
            
            visited.add((r,c))
            runningSum = 0
            #dirs = [(0,1),(0,-1),(1,0),(-1,0)]
            dirs = [(0,1),(1,0)]
            for d in dirs:
                runningSum += dfs(r+d[0], c+d[1], visited)

            visited.remove((r,c))
            dp[(r,c)] = runningSum

            return runningSum

        ret = dfs(0, 0, set())
        print(ret)
        return ret
    

sol = Solution()
sol.uniquePathsWithObstacles( [[0,0,0],[0,1,0],[0,0,0]])
sol.uniquePathsWithObstacles( [[0,1],[0,0]])
sol.uniquePathsWithObstacles([[0,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,1,0],[0,0,0,0]])