# TC: O(matrix): O(n^2) where n = len(matrix)
# Tanspose is O(n^2/2) since we are only traveseing through half the matrix O(n^2/2) rounds up to O(n^2)
# SwapCols is also O(n^2/2) since the outer loop only traverses through half the matrix O(n^2/2) rounds up to O(n^2)
# SC: O(1), we did not allocate additional memory

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # Rows become columns
        def transpose(matrix):
            for r in range(n):
                for c in range(r, n):
                    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        
        # For matrix cols 1,2,3 swap to become 3,2,1
        def swapCols(matrix):
            for col in range(n//2):
                left_col = col
                right_col = len(matrix)- 1 - col

                for row in range(n):
                    matrix[row][left_col], matrix[row][right_col] = matrix[row][right_col], matrix[row][left_col]

        print(matrix)
        transpose(matrix)
        print(matrix)
        swapCols(matrix)
        print(matrix)
        return matrix



# Transpose
# 1 4 7   
# 2 5 8
# 3 6 9

# Swap Columns