from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        found = False
        maxRow = len(board)
        maxCol = len(board[0])
        def dfs(board, ri, ci, word, visited):
            if word == "":
                return True
            if ri < 0 or ri >= maxRow:
                return False
            if ci < 0 or ci >= maxCol:
                return False

            if (ri, ci) in visited:
                return False
            curLetter = word[0]
            word = word[1:]   
            if board[ri][ci] != curLetter:
                return False
            
            dirs = [(0,1), (0,-1), (1,0), (-1,0)]
            for d in dirs:
                visited[(ri, ci)] = True
                tempRet = dfs(board, ri+d[0], ci+d[1], word, visited)
                if tempRet == True:
                    return True
                del visited[(ri, ci)]
            return False
        
        for ri, row in enumerate(board):
            for ci, col in enumerate(row):
                tempRet = dfs(board, ri, ci, word, {})
                if tempRet == True:
                    found = True
                    break
            if found == True:
                break
        print(found)
        return found




sol = Solution()
b1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word1 = "ABCCED"
sol.exist(b1, word1) # True

word2 = "SEE"
sol.exist(b1, word2) # True

word3 = "ABCB"
sol.exist(b1, word3) # False
