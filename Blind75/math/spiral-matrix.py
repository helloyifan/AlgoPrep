# 6 min, 6 min
from typing import List
# Given an m x n matrix, return all elements of the matrix in spiral order.

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        maxRow, maxCol = len(matrix), len(matrix[0])
        f,b = 0, maxCol 
        t,d = 0, maxRow 

        curLoc = [0,0]
        ret = []

        while f < b and t < d:
            # Go Right
            for i in range(f, b):
                curLoc[1] = i
                ret.append(matrix[curLoc[0]][curLoc[1]])
            t += 1

            if not (t < d):
                break


            # Go Down
            for i in range(t, d):
                curLoc[0] = i
                ret.append(matrix[curLoc[0]][curLoc[1]])
            b -= 1

            if not (f < b ):
                break

            # Go Left
            for i in range(b-1, f-1, -1):
                curLoc[1] = i
                ret.append(matrix[curLoc[0]][curLoc[1]])
            d -= 1
            if not (t < d):
                break
            
            # Go Up
            for i in range(d-1, t-1, -1):
                curLoc[0] = i
                ret.append(matrix[curLoc[0]][curLoc[1]])
            f += 1

        return ret
    
if __name__ == '__main__':
    sol = Solution()

    print(sol.spiralOrder([
        [1,2,3],
        [4,5,6],
        [7,8,9]]
        ))
    # [1,2,3,6,9,8,7,4,5]


    print(sol.spiralOrder([
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]]
        ))
    # [1,2,3,4,8,12,11,10,9,5,6,7]
    # [1,2,3,4,8, 12, 11, 10, 9, 5, 6, 7]
