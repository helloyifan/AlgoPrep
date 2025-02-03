from typing import List
from collections import deque

# Notes: BFS is better then DFS
# Think about the weird rules
# if the next step is out of bounds, dont try
# if we can walk to a wall, try it out
# BFS means when we find the first end, we can stop
# You need a visited set to avoid ending up at the same state

# TC: O(m*n*k)
# SC: O(m*n*k) # The visited set and the BFS queue also store at most O(m * n * k) states.

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        maxR = len(grid)-1
        maxC = len(grid[0])-1

        # kick start
        q = deque()
        q.append((0,0,k,(-1, -1), 0))

        minPath = float('inf')
        solved = False
        visited = set((0,0,k))

        while len(q) > 0:
            tempQ = deque()
            while len(q) > 0:
                node = q.pop()
                r, c, tempK, prev, steps = node[0], node[1], node[2], node[3], node[4]
                #print(r, c, tempK, prev, steps)

                if (r, c, tempK) in visited:
                    continue
                visited.add((r,c,tempK))

                if r == maxR and c == maxC:
                    minPath = min(minPath, steps)
                    solved = True
                    # This is the benefit of BFS, we dont need to explore rest of path
                    # This is literally the fastest one
                    break 
                    

                dirs = [(0,1), (0,-1), (1,0), (-1,0)]

                for d in dirs:
                    newR, newC = r+d[0], c+d[1]
                    # Exceeds bounds
                    if 0 > newR or newR > maxR or 0 > newC or newC > maxC:
                        continue

                    if grid[newR][newC] == 1:
                        if tempK > 0:
                            tempQ.append((newR, newC, tempK-1, (r,c), steps+1 ))
                
                    else:
                        tempQ.append((newR, newC, tempK, (r,c), steps+1))
            if solved == True:
                break
            q = tempQ

        if solved == False:
            minPath =  -1
        print(solved, minPath)
        return minPath
    
sol = Solution()
# sol.shortestPath( [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], 1)
# sol.shortestPath( [[0,1,1],[1,1,1],[1,0,0]], 1)
sol.shortestPath([[0,1,0,1],[0,1,0,0],[0,0,1,0],[1,0,0,1],[0,1,0,0]], 18)