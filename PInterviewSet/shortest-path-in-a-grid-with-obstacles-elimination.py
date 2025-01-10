from typing import List

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        lastR = len(grid) - 1
        lastC = len(grid[0]) - 1
        def dfs(r, c, k, visited):
            if (r,c) in visited:
                return False, -1

            if r < 0 or r > lastR:
                return False, -1            
            if c < 0 or c > lastC:
                return False, -1
            if r == lastR and c == lastC:
                print('bruh why no hit here mans')
                return True, 0

            visited.add((r,c))
            dirs = [(0,1), (0,-1), (1,0), (-1,0)]

            isPossible = False
            minDist = float('inf')

            for d in dirs:
                newR = r + d[0] 
                newC = r + d[1]
                
                if 0 <= newR and newR <= lastR:
                    if 0 <= newC and newC <= lastC:
                        if grid[newR][newC] == 1 and k > 0:
                            newIsPos, newMinDist = dfs(newR, newC, k-1, visited)

                            if newIsPos:
                                isPossible = True
                                minDist = min(minDist, newMinDist)

                        elif grid[newR][newC] == 0:
                            newIsPos, newMinDist = dfs(newR, newC, k, visited)

                            if newIsPos:
                                isPossible = True
                                minDist = min(minDist, newMinDist)

            visited.remove((r,c))


            return isPossible, minDist+1

        visited = set()
        retIsPos, ret = dfs(0, 0, k, visited)
        
        if not retIsPos:
            return -1
        
        return ret

sol = Solution()
print(sol.shortestPath([[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1))