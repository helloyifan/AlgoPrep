# Spent under 10 minutes,
# Could of used less memory but that would of taken more time

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowToFix =  []
        colToFix = []
        self.maxRow = len(matrix)
        self.maxCol = len(matrix[0])

        for ri, row in enumerate(matrix):
            for ci, col in enumerate(row):
                if matrix[ri][ci] == 0:
                    if ri not in rowToFix:
                        rowToFix.append(ri)
                    if ci not in colToFix:
                        colToFix.append(ci)
        
        # print(rowToFix)
        # print(colToFix)

        for ri in rowToFix:
            self.setRow(matrix, ri)

        for ci in colToFix:
            self.setCol(matrix, ci)

        return matrix
        
    def setRow(self, matrix, ri):
        for ci in range(0, self.maxCol):
            matrix[ri][ci] = 0

    def setCol(self, matrix, ci):
        for ri in range(0, self.maxRow):
            matrix[ri][ci] = 0


if __name__ == '__main__':
    sol = Solution()

    print(sol.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
    print(sol.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))