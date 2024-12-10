# Time Complexity
# Step 1. O(m*n) to identify all rotten
# Step 2. BFS could in explore all grid in worst case O(m*n)
# Step 3. O(m*n) to check for any unrotten
# Total O(3*m*n) = O(m*n)
# Space Compexity
# m*n grid = O(m*n)
# q could hold everything  = O(m*n)
# total  O(2*m*n) = O(m*n)
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        # Step 1 identiy all rotten
        for ir, r in enumerate(grid):
            for ic, c in enumerate(r):
                if c == 2: # rotten
                    q.append((ir, ic))

        dayCounter = 0
        
        # BFS to explore rottens 
        while len(q) > 0:
            #self.gridPrint(grid)
            replacementQ = []
            infectionHappendToday=False
            while len(q) >0:
                cur = q.pop()
                dirs = [(0,1),(1,0),(0,-1),(-1,0)]
                for dir in dirs:
                    adjRow = cur[0]+dir[0]
                    adjCol = cur[1]+dir[1]
                    if 0 <= adjRow < len(grid) and 0<= adjCol < len(grid[0]):
                        if grid[adjRow][adjCol] == 1: # fresh to be made rotten
                            infectionHappendToday = True
                            grid[adjRow][adjCol] = 2
                            replacementQ.append((adjRow, adjCol))
            q = replacementQ
            
            # only count the day up if we did any rotting
            if infectionHappendToday:
                dayCounter +=1

        for ir, r in enumerate(grid):
            for ic, c in enumerate(r):
                if c == 1: # couldnt rot it
                    dayCounter = -1 # cant solve it so its -1
        
        print(dayCounter)
        return dayCounter
    
    def gridPrint(self, grid):
        for r in grid:
            print(r)
        print('---')
sol = Solution()
sol.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
sol.orangesRotting([[2,1,1],[0,1,1],[1,0,1]])
sol.orangesRotting([[0,2]])