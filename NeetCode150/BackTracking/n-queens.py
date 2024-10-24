from typing import List
from collections import defaultdict
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # setup
        board = [['.' for _ in range(n) ] for _ in range(n)]

        # sparce matrix
        queens = defaultdict(dict) 
        # not so sure about this data strucutre, bcuz if r in queens doesnt make sense, what if 
        # we cerated the nested dict bcuz it was at one point empty

        # we hsould use
        row = set()
        col = set()
        onTheBoardSoFar = set()
        ret = []
        def backTrack(remainingQueens):
            if remainingQueens == 0:
                return True
            
            for r in range(n):
                for c in range(n):                       

                    if self.validation(row, col, onTheBoardSoFar, n, r, c):
                        row.add(r)
                        col.add(c)
                        onTheBoardSoFar.add((r,c))
                        tempRet = backTrack(remainingQueens-1)
                        if tempRet == True:
                            # Write this to ret
                            ret.append([r,c])
                            return True
                        
                        row.remove(r)
                        col.remove(c)
                        onTheBoardSoFar.remove((r,c))
            return ret
        
        backTrack(n)
        print(ret)
        return
    
    def boardPrinter(board):
        for row in board:
            print(row)
    

    def validation(self, row, col, onTheBoardSoFar, n, r, c):
        # check to see if row is populated
        if r in row:
            return False

        # check to see if col is populated        
        if c in col:
            return False
        
        # Todo calculate diagons

        ## This needs debugging
        if not (self.diagnoalValidations(onTheBoardSoFar, n, r, c)):
            return False

        return True

    ## This needs debugging
    def diagnoalValidations(self, onTheBoardSoFar, n, r, c):
        dirs = [(1,1), (1,-1), (-1, 1), (-1, -1)]

        for d in dirs:
            incrementR = r + d[0]
            incrementC = c + d[1]
            while (-1 < incrementR < n) and (-1 < incrementC < n):
                if (incrementR, incrementC) in onTheBoardSoFar:
                    return False

                incrementR += d[0]
                incrementC += d[1]
        
        return True


# diag conds

# r, c
# r + 1, c +1
# r -1, c -1
# r + 1, c -1
# r- 1, c + 1

sol = Solution()
sol.solveNQueens(4)
# Result 4

# testSet = set()
# testSet.add((0,0))
# testSet.add((1,1))
# testSet.add((2,2))
# print(sol.diagnoalValidations(testSet, 4, 3, 3))

#testSet = set()
#testSet.add((2,2))
#print(sol.diagnoalValidations(testSet, 4, 1, 2))
