from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        veinCounter = 0
        for rowInd, rowVal in enumerate(grid):
            for colInd, colVal in enumerate(rowVal):
                if (grid[rowInd][colInd] == "1"):
                    self.clearVein(grid, rowInd, colInd)
                    veinCounter +=1

                    #print(grid)
        return veinCounter

    def clearVein(self, grid: List[List[str]], row: int, col: int):
        if (row >= len(grid) or 
            col >= len(grid[0]) or 
            row < 0 or
            col < 0 or 
            grid[row][col] == "0"
        ):
            return
        # Create cell
        grid[row][col] = "0"

        # Recursion down
        self.clearVein(grid, row +1, col)

        # Recursion right
        self.clearVein(grid, row, col+1)

        # Recursion up 
        self.clearVein(grid, row - 1, col)

        # Recursion left
        self.clearVein(grid, row, col - 1)


        return

s = Solution()

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
r1 = s.numIslands(grid)
print(r1)

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
r2 = s.numIslands(grid2)
print(r2)

grid3 = [
  ["1","1","0","0","0"]
]
r3 = s.numIslands(grid3)
print(r3)

grid4 = [
  ["1"]
]
r4 = s.numIslands(grid4)
print(r4)

grid5 = [
  []
]
r5 = s.numIslands(grid5)
print(r5)

grid6 = [
    ["1","1","1"],
    ["0","1","0"],
    ["1","1","1"]
]
r6 = s.numIslands(grid6)
print(r6)