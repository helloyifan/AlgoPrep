# Note difference betwee n search-a-2d-matrix 1 and 2 is that, 
# 1 the last elemnt of one row is lesser then first element of next row

# Not here this is for search-a-2d-matrix2
'''
matrix = [
[1,4,7,11,15],
[2,5,8,12,19],
[3,6,9,16,22],
[10,13,14,17,24],
[18,21,23,26,30]

], target = 5
'''

# TC: 0(m*logn) where m is the nubmer of rows and n is the number of columns
# SC: O(1) we dont use additional data structures
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for row in matrix:
            if row[0] <= target and target <= row[len(row)-1]:

                l, r =0, len(row) -1

                while l <= r:
                    median = (l+r)//2

                    if row[median] > target:
                        r = median -1
                    elif row[median] < target:
                        l = median + 1
                    else: # row[median] == target:
                        return True
        
        return False