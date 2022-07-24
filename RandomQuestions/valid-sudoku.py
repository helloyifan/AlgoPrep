from typing import List

##: 11:40 - 12:45
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for y, row in enumerate(board):
            for x, col in enumerate(row):
                if (board[y][x] == '.'):
                    continue
                ret = self.check(board, x, y)
                if (ret == False):
                    return False
        return True

    def check(self, board, x, y):

        r1 = self.check_row(board, x, y)
        if (r1 == False):
            #print('check_row')
            return False
        r2 = self.check_col(board, x, y)
        if (r2 == False):
            #print('check_col')
            return False
        r3 = self.check_block(board, x, y)    
        if (r3 == False):
            #print('check_block')
            return False

        return True
        
    def check_row(self, board, x, y):
        spot = board[y][x]
        row = board[y]
        for i, val in enumerate(row):
            if (i == x):
                continue # skip checking the same col
            if (spot == val):
                return False
        return True
    
    def check_col(self, board, x, y):
        spot = board[y][x]
        
        for i, row in enumerate(board):
            if (i == y): #if we are checking all the cols, avoid checking the col where our input (x,y) is in
                continue # skip checking the same row
            if (spot == row[x]):
                return False
        return True
    
    def check_block(self, board, x, y):
        spot = board[y][x]

        x_block_start = int(x/3) * 3 
        y_block_start = int(y/3) * 3 

        for i in range(x_block_start, x_block_start + 3):
            for j in range(y_block_start, y_block_start + 3):
                if (j == y and i == x):
                    continue # skip checking the same spot we are on
                if (spot == board[j][i]):
                    return False
        return True


sol = Solution()
board1 = [
 ["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]
]
board2 = [
 ["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
r1 = sol.isValidSudoku(board1)
print(r1)

r2 = sol.isValidSudoku(board2)
print(r2)