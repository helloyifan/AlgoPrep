from typing import List

# Tried for 30 mins, got confused and stuck
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        for ri, re in enumerate(grid):
            for ci, ce in enumerate(re):
                if ce == 0:
                    self.recursivelyMoveAround(ri, ci, grid)

        return

    def recursivelyMoveAround(self, ri, ci, grid):
        maxR, maxC = len(grid), len(grid[0])
        
        
        q = []
        q.append((ri, ci))
        stepsAway = 0 

        replaceMentQ = []
        while len(q) > 0 or len(replaceMentQ) > 0:
            self.printGrid(grid)
            
            while len(q) > 0:
                #print(q)
                c = q.pop(0)
                v = grid[c[0]][c[1]]

                if v == -1:
                    continue
                if v == 0 and stepsAway > 0:
                    continue
                
                if v == 2147483647:
                    print("hit")
                    grid[c[0]][c[1]] = stepsAway # for first time we set it from 0 to 0?


                dirs = [(0,-1), (0,1), (-1,0), (1,0)]
                for dir in dirs:
                    newRow = c[0] + dir[0]
                    newCol = c[1] + dir[1]
                    if newRow >= 0 and newRow < maxR and newCol >= 0 and newCol < maxC:
                        replaceMentQ.append((newRow, newCol))
                
            # done with the current round, setup for next round
            q = replaceMentQ[:]
            stepsAway += 1

        return 

    def printGrid(self, grid):
        for r in grid:
            print(r)
        print('----')



if __name__ == "__main__":
    sol = Solution()
    input1 = [
        [2147483647,-1,0,2147483647],
        [2147483647,2147483647,2147483647,-1],
        [2147483647,-1,2147483647,-1],
        [0,-1,2147483647,2147483647]
    ]
    sol.islandsAndTreasure(input1)