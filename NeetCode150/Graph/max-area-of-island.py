from typing import List

#Solved in like 15mins
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxRow = len(grid) -1
        maxCol = len(grid[0]) -1

        def countAndFlip(ri, ci):
            if ri < 0 or ri > maxRow or ci < 0 or ci > maxCol:
                return 0
            if grid[ri][ci] == 0:
                return 0
            
            count = 0
            if grid[ri][ci] ==  1:
                count +=1 
                grid[ri][ci] = 0 

            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dir in dirs:
                count += countAndFlip(ri + dir[0], ci + dir[1])
            
            return count

        maxRet = 0
        for ri, re in enumerate(grid):
            for ci, ce in enumerate(re):
                maxRet = max(maxRet, countAndFlip(ri, ci))

        print(maxRet)
        return maxRet


if __name__ == "__main__":

    sol = Solution()
    grid = [
        [0,1,1,0,1],
        [1,0,1,0,1],
        [0,1,1,0,1],
        [0,1,0,0,1]
    ]
    sol.maxAreaOfIsland(grid)