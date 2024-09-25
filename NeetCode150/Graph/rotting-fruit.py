from typing import List
# Attempted 15 min, but was unable to submit, base case of 0 is -1 is weird
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
    
        def infestOneCycle(grid):
            rl = len(grid)
            cl = len(grid[0])

            madeInfestationThisCycle = False

            for ri, row in enumerate(grid):
                for ci, col in enumerate(row):
                    if col == 2:
                        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

                        for d in dirs:
                            tempRi = ri + d[0]
                            tempCi = ci + d[1]

                            if 0 <= tempCi < cl and 0 <= tempRi < rl and grid[tempRi][tempCi] == 1:
                                grid[ri + d[0]][ci + d[1]] = 2
                                madeInfestationThisCycle = True
            
            return madeInfestationThisCycle
            
        #self.printGrid(grid)
        
        newInfesticationMade = True
        cyclesOfInfestation = 0 
        while newInfesticationMade:
            newInfesticationMade = infestOneCycle(grid)
            if newInfesticationMade:
                cyclesOfInfestation += 1
            
            #print('-------')
            #self.printGrid(grid)

        if cyclesOfInfestation == 0:
            cyclesOfInfestation =  -1
        print(cyclesOfInfestation)
        return cyclesOfInfestation 

    def printGrid(self, grid):
        for row in grid:
            print(row)
        return

sol = Solution()
sol.orangesRotting([[1,1,0],[0,1,1],[0,1,2]]) # 4
sol.orangesRotting([[1,0,1],[0,2,0],[1,0,1]]) # -1