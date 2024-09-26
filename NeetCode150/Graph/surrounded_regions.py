from typing import List

# The condition should be, 
# if O, use DFS to determine if it touches any boarders
# if it doesn't, fill


# Solved in 30 min, had to use debugger
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        outOfBoundRow = len(board)
        outOfBoundCol = len(board[0]) 
        
        def dfs(ri, ci, visited) -> bool: # Returns should be filled bool
            if (ri, ci) in visited:
                return True

            visited.add((ri, ci))
            print((ri, ci))
            if ri == -1 or ri == outOfBoundRow:
                return False
            if ci == -1 or ci == outOfBoundCol:
                return False # hit a boarder, so its not surrounded by X
            
            if board[ri][ci] == 'X':
                return True # this is surronded by X, so this boarder

            dirs = [(0,1), (0,-1), (1,0), (-1,0)]
            for d in dirs:
                newRi = ri + d[0]
                newCi = ci + d[1]
                shouldBeFilled = dfs(newRi, newCi, visited)

                if not shouldBeFilled:
                    return False #which is false
            
            return True

        def dfsFill(ri, ci, visited):
            if (ri, ci) in visited:
                return 

            visited.add((ri, ci))
            if ri == -1 or ri == outOfBoundRow or ci == -1 or ci == outOfBoundCol:
                return
            if board[ri][ci] != 'O':
                return
            board[ri][ci] = 'X'

            dirs = [(0,1), (0,-1), (1,0), (-1,0)]
            for d in dirs:
                newRi = ri + d[0]
                newCi = ci + d[1]
                dfsFill(newRi, newCi, visited)

            return


        for ri, row in enumerate(board):
            for ci, col in enumerate(row):
                if board[ri][ci] == "O":
                    #print("---")
                    shouldFill = dfs(ri, ci, set())
                    if shouldFill: #should be filled
                        dfsFill(ri, ci, set())

        #self.printGrid(board)
        #print('------')
        return 
    
    def printGrid(self, board):
        for row in board:
            print(row)

sol = Solution()
sol.solve([
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","O","O","X"],
  ["X","X","X","O"]
])

# sol.solve([
#   ["X","X","X","X"],
#   ["X","X","X","X"],
#   ["X","X","X","X"],
#   ["X","X","X","O"]
# ])