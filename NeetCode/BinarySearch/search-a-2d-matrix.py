from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        numRows = len(matrix)
        numCols = len(matrix[0])

        #print('numRows:', numRows, "numCols:", numCols)

        for i in range(numRows):
            if (target <= matrix[i][numCols-1]):
                ## Binary search time
                h, t = 0 , numCols-1
                while (h <= t):
                    m = (h + t) // 2

                    if (matrix[i][m] < target ):
                        h = m + 1
                    elif (matrix[i][m] > target):
                        t = m - 1
                    else:
                        return True
                break
        return False


s = Solution()

# matrix1 = [
#     [1,3,5,7],
#     [10,11,16,20],
#     [23,30,34,60]
# ]
# target1 = 3
# r1 = s.searchMatrix(matrix1, target1)
# print(r1)

# matrix2 = [
#     [1,3,5,7],
#     [10,11,16,20],
#     [23,30,34,60]
# ]
# target2 = 13
# r2 = s.searchMatrix(matrix2, target2)
# print(r2)


matrix3 = [
    [1]
]
target3 = 1
r3 = s.searchMatrix(matrix3, target3)
print(r3)
