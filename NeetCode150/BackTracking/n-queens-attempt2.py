# VALID Effort, passed 7/9 tests on Leetcode (due to TLE) 
# But this question is too strict that i need to have the exact correct solution to pass otherwise it will fail to TLE
# From attempt 1 to attempt 2, i build the solution bottom upinstead of top down
    # not a big difference just code cleanliness
# Another improvment is the observation of r+c and r-c for the diags
from typing import List
import copy
from collections import defaultdict
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]

        row = set()
        col = set()
        posDiag = set()
        negDiag = set()

        ret = []
        visited = []
        visitedBoards = set()
        def dfs(numOfQueens):
            if numOfQueens == n:
                visitedCopy = copy.deepcopy(visited)
                visitedCopy.sort()
                visitedTuple = tuple(visitedCopy)
                #print(visitedCopy)
                if not visitedTuple in visitedBoards:
                    temp = copy.deepcopy(board)
                    ret.append(temp)
                    visitedBoards.add(visitedTuple)
                return
            
            for r in range(n):
                for c in range(n):
                    if self.validation(row, col ,posDiag, negDiag, r ,c):
                        row.add(r)
                        col.add(c)
                        posDiag.add(r+c)
                        negDiag.add(r-c)
                        board[r][c] = 'Q'
                        visited.append((r,c))

                        dfs(numOfQueens+1)

                        row.remove(r)
                        col.remove(c)
                        posDiag.remove(r+c)
                        negDiag.remove(r-c)
                        board[r][c] = '.'
                        visited.pop() # question is pop O(n)
            return
        
        dfs(0)

        finRet = []
        for b in ret:
            curBoardRet = []
            for r in b:
               curBoardRet.append("".join(r))
            
            finRet.append(curBoardRet)
        
        for b in finRet:
            self.boardPrinter(b)

        return finRet
    

    def validation(self, row, col, posDiag, negDiag, r, c):
        if r in row:
            return False
        
        if c in col:
            return False
        
        if r+c in posDiag:
            return False
        
        if r-c in negDiag:
            return False
        
        return True
    
    def boardPrinter(self, board):
        for r in board:
            print(r)
        print('----')

        

sol = Solution()
# sol.solveNQueens(4)
sol.solveNQueens(5)
