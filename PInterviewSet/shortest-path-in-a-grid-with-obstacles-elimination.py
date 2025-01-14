from typing import List
from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        lastR, lastC = len(grid)-1, len(grid[0])-1
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        q = deque() #(r,c,k)
        q.appendleft((0,0,k))
        numOfSteps = 0
        doneFlag = False
        visited = set((0,0,k))
        while len(q) >0:
            tempQ = deque()
            while len(q) > 0:
                h = q.pop()
                r,c,curK = h[0], h[1], h[2]

                if (r,c,curK) in visited:
                    continue

                visited.add((r,c,k))

                if r == lastR and c == lastC:
                    doneFlag = True
                    break

                for d in dirs:
                    newR, newC = r + d[0], c + d[1]

                    # Validations
                    if (0 <= newR <= lastR) and (0 <= newC <= lastC):
                        if grid[newR][newC] == 1:
                            if curK > 0:
                                tempQ.appendleft((newR,newC,curK-1))
                        elif grid[newR][newC] == 0:
                            tempQ.appendleft((newR,newC,k))
            if doneFlag:
                break
            q = tempQ
            numOfSteps += 1

        if doneFlag == False:
            return -1

        return numOfSteps

sol = Solution()
print(sol.shortestPath([[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], 1)) # 6
print(sol.shortestPath([[0,1,1],[1,1,1],[1,0,0]], 1)) # -1
print(sol.shortestPath([[0,0,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,0],[0,1,0,0,0,0,0,0,0,0],[0,1,0,1,1,1,1,1,1,1],[0,1,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,0],[0,1,0,0,0,0,0,0,0,0],[0,1,0,1,1,1,1,1,1,1],[0,1,0,1,1,1,1,0,0,0],[0,1,0,0,0,0,0,0,1,0],[0,1,1,1,1,1,1,0,1,0],[0,0,0,0,0,0,0,0,1,0]]
, 1)) # 20