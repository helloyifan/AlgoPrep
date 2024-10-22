from typing import List
from collections import defaultdict
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # setup
        board = [['.' for _ in range(n) ] for _ in range(n)]

        startV = 0
        endV =  n-1

        # sparce matrix
        queens = defaultdict(dict) # not so sure about this data strucutre, bcuz if r in queens doesnt make sense, what if 
        # we cerated the nested dict bcuz it was at one point empty

        # we hsould use
        row = set()
        col = set()

        def backTrack(remainingQueens):
            if remainingQueens == 0:
                return True
            for r in range(n):
                for c in range(n):
                    if self.validation(queens,r ,c):
                        queens[r][c] = True
                        tempRet = backTrack(remainingQueens-1)
                        if tempRet == True:
                            return True
                        del queens[r][c]
            return 
        
        backTrack(n)
        print(queens)
        return
    
    def boardPrinter(board):
        for row in board:
            print(row)
    

    def validation(self, queens, r, c):
        # check to see if row is populated
        if r in queens:
            return False

        # check to see if col is populated        
        for row in queens:
            if c in row:
                return False



sol = Solution()
sol.solveNQueens(4)
# Result 4

