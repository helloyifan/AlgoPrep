
class ValidSudoku():

    def valid_sudoku(self, board):
        if not self.check_horizontal(board):
            print('not horizontal')
            return False
        
        if not self.check_vertical(board):
            print('not vertical')
            return False
        
        if not self.check_grid(board):
            print('not grid')
            return False
        


    def check_horizontal(self, board):
        for r in board:
            if not self.check_if_list_valid(r):
                return False
        return True
    
    def check_vertical(self, board):
        for i in range(0, 9):
            list = []
            for j in range(0,9):
                list.append(board[j][i])    
            
            if not self.check_if_list_valid(list):
                return False
        return True
    
    def check_grid(self, board):
        for i in range(0,9,3):
            for j in range (0, 9 ,3):
                list = self.get_small_grid(board, i, j)
                if not self.check_if_list_valid(list):
                    return False
        return True

    def get_small_grid(self, board, start_r, start_c):
        list = []

        for i in range(0,3):
            for j in range(0,3):
                list.append(board[start_r + i][start_c + j])
        return list

    def check_if_list_valid(self, list):
        check_list = []
        for i in list:
            if i in check_list:
                return False
            
            if i != '.':
                check_list.append(i)
        return True
    


    def sudoku_printer(board):
        for r in board:
            print(r)

if __name__ == "__main__":
    sol = ValidSudoku()

    board = [
        ["1","2",".",".","3",".",".",".","."],
        ["4",".",".","5",".",".",".",".","."],
        [".","9","8",".",".",".",".",".","3"],
        ["5",".",".",".","6",".",".",".","4"],
        [".",".",".","8",".","3",".",".","5"],
        ["7",".",".",".","2",".",".",".","6"],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".","4","1","9",".",".","8"],
        [".",".",".",".","8",".",".","7","9"]
    ]

    sol.valid_sudoku(board)

    