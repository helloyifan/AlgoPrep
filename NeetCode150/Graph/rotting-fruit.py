from typing import List
# Attempted 15 min, but was unable to submit
# Spend another 5 min debugging edge csaes
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
    
        def infestOneCycle(grid):
            rl = len(grid)
            cl = len(grid[0])

            madeInfestationThisCycle = False
            infectedInCurrentCycle = []
            for ri, row in enumerate(grid):
                for ci, col in enumerate(row):
                    if col == 2:
                        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

                        for d in dirs:
                            tempRi = ri + d[0]
                            tempCi = ci + d[1]

                            if 0 <= tempCi < cl and 0 <= tempRi < rl and grid[tempRi][tempCi] == 1:
                                infectedInCurrentCycle.append((ri + d[0], ci + d[1]))
                                madeInfestationThisCycle = True
            # execute the infection
            for i in infectedInCurrentCycle:
                grid[i[0]][i[1]] = 2

            return madeInfestationThisCycle
            
        # self.printGrid(grid)
        
        newInfesticationMade = True
        cyclesOfInfestation = 0 
        while newInfesticationMade:
            newInfesticationMade = infestOneCycle(grid)
            if newInfesticationMade:
                cyclesOfInfestation += 1
            
            # print('-------')
            # self.printGrid(grid)

        # check to see if theres any uninfected left
        for row in grid:
            for col in row:
                if col == 1:
                    return -1
        return cyclesOfInfestation 

    def printGrid(self, grid):
        for row in grid:
            print(row)
        return

sol = Solution()
print(sol.orangesRotting([[1,1,0],[0,1,1],[0,1,2]]))# 4
print(sol.orangesRotting([[1,0,1],[0,2,0],[1,0,1]])) # -1
print(sol.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])) # 4
print(sol.orangesRotting([[2,1,1],[0,1,1],[1,0,1]])) # -1
print(sol.orangesRotting([[0,2]])) # 0