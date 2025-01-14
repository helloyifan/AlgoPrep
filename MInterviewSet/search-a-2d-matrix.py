# This is a of sorted strings broken down in a matrix, 
# Where the last element of row is lesser then all elements of the next row

# Test input
# matrix = [
# [1,3,5,7],
# [10,11,16,20],
# [23,30,34,60]
#]

# Different from search-a-2d-matrix2

# Notes: Do binary search on r=0, l = (m*n)-1
# Keep good track of row and col of the medain (double check)
# TC: O(log(m*n)) - we are performing binary search on a space of m*n
# SC: O(1) we are not using any additional data structures
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) #num of cols
        n = len(matrix[0]) #mum of row

        l, r =0, (m*n)-1

        while l <= r:
            median = (l+r)//2

            medianR, medianC = median // n, median % n

            if matrix[medianR][medianC] > target:
                r = median-1
            elif matrix[medianR][medianC] < target:
                l =  median+1
            else: #Found
                return True

        return False