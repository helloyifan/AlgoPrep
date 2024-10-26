from typing import List
import copy
from collections import defaultdict
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]

        col = set()
        #row = set() # not need ;)

        posDiag = set()
        negDiag = set()

        ret = []
        def dfs(numOfQueens):
            if numOfQueens == n:
                copyBoard = copy.deepcopy(board)
                ret.append(copyBoard)
                return
            
            # Logic is, since theres no 2 queens on the same R
            # if we are checking all c, then no need to iterate over it
            r = numOfQueens #i dont get this
            for c in range(n):
                if self.valid(col, posDiag, negDiag, r, c):

                    # Change states
                    col.add(c)
                    posDiag.add(r + c)
                    negDiag.add(r - c)
                    board[r][c] = 'Q'

                    dfs(numOfQueens+1)
                    
                    #Clean up states
                    col.remove(c)
                    posDiag.remove(r + c)
                    negDiag.remove(r - c)
                    board[r][c] = '.'
            return
        dfs(0)

        # for r in ret:
        #     self.boardPinter(r)
        
        ## Ret building

        finRet = []

        for r in ret:
            curFinRet = []
            for row in r:
                curFinRet.append("".join(row))
            finRet.append(curFinRet)

        # for f in finRet:
        #     self.boardPinter(f)

        return finRet

    def boardPinter(self, board):
        for r in board:
            print(r)
        print('----')

    def valid(self, col, posDiag, negDiag, r, c):
        if c in col:
            return False
        
        if r+c in posDiag:
            return False
        
        if r-c in negDiag:
            return False
        
        return True
        

sol = Solution()
#sol.solveNQueens(4)
sol.solveNQueens(5)
