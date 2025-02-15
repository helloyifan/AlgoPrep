# Notes: A good interested backtrack question, my intuition was to keep track of count which was also correct
# TC: 4^(m*n), each gripd we have 4 diretions
# SC: O(m*m) for keeping track of path

from typing import List
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        maxR, maxC = len(grid)-1, len(grid[0]) -1

        startR, startC = None, None
        count = 1 # start with one extra step for the start
        result = []

        for ri, row in enumerate(grid):
            for ci, col in enumerate(row):
                if grid[ri][ci] == 1:
                    startR, startC = ri, ci
                elif grid[ri][ci] == 0:
                    count +=1
        print(count)
        def dfs(r, c, path):
            nonlocal count
            nonlocal result

            if r < 0 or r > maxR or c < 0 or c > maxC:
                return False
            
            if grid[r][c] == -1:
                return False
            
 
            if count == 0 and grid[r][c] != 2:
                return False
            
            if grid[r][c] == 2 and count != 0:
                return False
            
            if grid[r][c] == 2 and count == 0:
                print('yep')
                result.append(path[:])
                return True
            
            path.append((r,c))
            grid[r][c] = -1

            dirs = [(0, 1),(0,-1),(1,0),(-1,0)]
            for d in dirs:
                count -= 1
                dfs(r+d[0], c+d[1], path)
                count += 1

            path.pop()
            grid[r][c] = 0

            return
        
        dfs(startR, startC, [])
        print(result)
        print(grid)
        return len(result)
    

sol = Solution()
sol.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]])