# Attempt 1, recursive unscalable solution (45  min distracted)
# Time complexity: O(m*n*( 4^m*n)) # 
# m*n for the first for loops, and for each cell, we have 4 directions which has a depth of m*n

# Space complexity
# O(m*n) for stack usage because of recursion depth
from typing import List
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        #dp = {}

        maxRet = float('-inf')
        for ir, r in enumerate(matrix):
            for ic, c in enumerate(r):
                visited = set()
                matrixStart = (ir, ic)
                print("matrixStart: ", matrixStart)
                tempRet = self.dfsExplorer(matrix, matrixStart, visited)
                maxRet = max(maxRet, tempRet)
        
        return maxRet


    def dfsExplorer(self, matrix, matrixStart, visited):        
        # if matrixStart in visited: #This is actually flawed idea
        #     return 0

        visited.add(matrixStart)

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        maxRet = 0
        for d in dirs:
            nextStep = (matrixStart[0] + d[0], matrixStart[1] + d[1])

            if nextStep[0] < 0 or nextStep[0] >= len(matrix):
                continue
            
            if nextStep[1] < 0 or nextStep[1] >= len(matrix[0]):
                continue            
            
            msVal = matrix[matrixStart[0]][matrixStart[1]]
            nsVal = matrix[nextStep[0]][nextStep[1]]
            if msVal < nsVal:
                maxRet = max(maxRet, self.dfsExplorer(matrix, nextStep, visited))
        return maxRet + 1


sol = Solution()
# sol.longestIncreasingPath(
#     [[5,5,3],
#      [2,3,6],
#      [1,1,1]]
# )# Ret is 4 ([1, 2, 3, 6] or [1, 2, 3, 5].)


# sol.longestIncreasingPath(
#     [[1,2,3],
#      [2,1,4],
#      [7,6,5]]
# )# Ret is 7

sol.longestIncreasingPath(
    [[7,6,1,1],
     [2,7,6,0],
     [1,3,5,1],
     [6,6,3,2]]
)# Ret is 7

