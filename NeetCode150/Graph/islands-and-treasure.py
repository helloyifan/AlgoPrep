from typing import List

# Tried for 30 mins, got confused and stuck
# Tried for 20min, the solution is not great but it passes
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        for ri, re in enumerate(grid):
            for ci, ce in enumerate(re):
                if ce == 0:
                    self.itrativelyMoveAround(ri, ci, grid)

        return

    def itrativelyMoveAround(self, ri, ci, grid):
        maxR, maxC = len(grid), len(grid[0])
        traversed = set()
        
        stepsAway = 0

        nq = []
        nq.append((ri, ci))

        while len(nq) > 0:
            q = nq[:]
            nq = []

            while len(q) > 0:
                curNode = q.pop(0)
                traversed.add(curNode)

                # handle cur step
                if grid[curNode[0]][curNode[1]] > stepsAway:
                    grid[curNode[0]][curNode[1]] = stepsAway

                # handle next steps
                dirs = [(0,1), (0,-1), (1, 0), (-1, 0)]
                for dir in dirs:
                    newR = curNode[0] + dir[0]
                    newC = curNode[1] + dir[1]
                    if newR >= 0 and newR < maxR and newC >=0 and newC < maxC:
                        if not (newR, newC) in traversed:
                            if grid[newR][newC] != 0 and grid[newR][newC] != -1:
                                nq.append((newR, newC))

            stepsAway += 1
        #self.printGrid(grid)
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

    input2 =  [
        [0,-1],
        [2147483647,2147483647]
    ]
    sol.islandsAndTreasure(input2)

