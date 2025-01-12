# DFS solution that leverage DP, it works but doesnt satify runtime
from typing import List

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        dp = {} #(): val
        lastR = len(grid) - 1
        lastC = len(grid[0]) - 1
        def dfs(r, c, k, visited, dp):
            if (r,c,k,len(visited)) in dp:
                tempRet = dp[(r,c,k,len(visited))]
                print('hit')
                return tempRet[0], tempRet[1]

            if (r,c) in visited:
                return False, -1

            if r < 0 or r > lastR:
                return False, -1            
            if c < 0 or c > lastC:
                return False, -1

            if r == lastR and c == lastC:
                return True, 0

            visited.add((r,c))
            dirs = [(0,1), (0,-1), (1,0), (-1,0)]

            isPossible = False
            minDist = float('inf')
            for d in dirs:
                newR = r + d[0] 
                newC = c + d[1]

                if newR >= 0 and newR <= lastR:
                    if newC >= 0 and newC <= lastC:
                        if grid[newR][newC] == 1 and k > 0:
                            newIsPos, newMinDist = dfs(newR, newC, k-1, visited, dp)

                            if newIsPos:
                                isPossible = True
                                minDist = min(minDist, newMinDist)

                        elif grid[newR][newC] == 0:
                            newIsPos, newMinDist = dfs(newR, newC, k, visited, dp)

                            if newIsPos:
                                isPossible = True
                                minDist = min(minDist, newMinDist)

            visited.remove((r,c))

            dp[(r,c,k,len(visited))] = (isPossible, minDist+1)

            return isPossible, minDist+1

        visited = set()
        retIsPos, ret = dfs(0, 0, k, visited, dp)
        if not retIsPos:
            return -1
        
        return ret

sol = Solution()
print(sol.shortestPath([[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], 1)) # 6
print(sol.shortestPath([[0,1,1],[1,1,1],[1,0,0]], 1)) # -1
print(sol.shortestPath([[0,0,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,0],[0,1,0,0,0,0,0,0,0,0],[0,1,0,1,1,1,1,1,1,1],[0,1,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,0],[0,1,0,0,0,0,0,0,0,0],[0,1,0,1,1,1,1,1,1,1],[0,1,0,1,1,1,1,0,0,0],[0,1,0,0,0,0,0,0,1,0],[0,1,1,1,1,1,1,0,1,0],[0,0,0,0,0,0,0,0,1,0]]
, 1)) # -1