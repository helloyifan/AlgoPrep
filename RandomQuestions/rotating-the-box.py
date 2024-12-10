from typing import List
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        oldRowLen, oldColLen = len(box), len(box[0])
        newBox = [['' for _ in range(oldRowLen)] for _ in range(oldColLen)]
        newRowLen, newColLen = len(newBox), len(newBox[0])
        # Rotate
        for ir, r in enumerate(box):
            for ic, c in enumerate(r):
                newBox[ic][newColLen -1 -ir] = c

        # self.printBcuzImStupid(newBox)
        # print('cock')
        # Execute gravity
        # Bottom up style

        for ir2 in range(len(newBox)-1, -1 ,-1):
            # I dont think it matters for the column, if we go front to back vs reverse
            for ic2 in range(len(newBox[0])):
                unitsItCanMoveDown = self.canMoveDown(ir2, ic2, newBox)
                if unitsItCanMoveDown > 0:
                    newBox[ir2][ic2] = '.'
                    newBox[ir2+unitsItCanMoveDown][ic2] = '#'
        
        self.printBcuzImStupid(newBox)

        return newBox
    
    def canMoveDown(self, r, c, b):
        # We only move hashtags
        if b[r][c] != "#":
            return 0

        unitsItCanMoveDown = 0

        while True:
            # At bottom
            if r + unitsItCanMoveDown == len(b)-1:
                return unitsItCanMoveDown
            # Something is blocking
            if b[r+unitsItCanMoveDown + 1][c] == "#" or b[r+unitsItCanMoveDown + 1][c] == "*":
                return unitsItCanMoveDown            
            unitsItCanMoveDown+=1 
        return "huh"

    def printBcuzImStupid(self, b):
        for r in b:
            print(r)
        return
sol = Solution()
#sol.rotateTheBox([["#",".","#"]])
sol.rotateTheBox(
    [["#",".","*","."],
    ["#","#","*","."]]
)
# sol.rotateTheBox([
#     ["#","#","*",".","*","."],
#     ["#","#","#","*",".","."],
#     ["#","#","#",".","#","."]]
# )