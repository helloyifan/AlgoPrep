# This question is actually very confusing if we want to use no space
# The primary hint would be to draw it out (where each cell goes next)
# Make 4 moves at a time (bcuz its a square)

# Time for attempt 1
# 1hour+ 

class Solution(object):
    def printMatrix(self, matrix):
        print('---')
        for r in matrix:
            print(r)

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        minV = 0
        maxV = len(matrix) - 1

        while minV < maxV:
            for i in range(minV, maxV ):
                self.circleRotateThisIndex(matrix, minV, maxV, minV, i)

            minV += 1
            maxV -= 1

        # self.printMatrix(matrix)
        return matrix


    # R: row of first element
    # C: col of first element
    def circleRotateThisIndex(self, matrix, minV, maxV, r, c,):

        temp = matrix[r][c]
        # Move 1: Top to Right
        r = c
        c = maxV
        temp = self.swap(matrix, r, c, temp)

        #Move 2: Right to Bottom
        t = abs(minV - r) # This is to account for the offset from the corner
        r = c
        c = maxV - t
        temp = self.swap(matrix, r, c, temp)
        
        # Move 3: Bottom to Left
        r = c
        c = minV
        temp = self.swap(matrix, r, c, temp)

        # Move 4: 
        t = abs(minV - r)
        r = c
        c = maxV - t
        temp = self.swap(matrix, r, c, temp)

        return
    
    def swap(self, matrix, r, c, temp):
        temp2 = matrix[r][c]
        matrix[r][c] = temp
        return temp2
    
if __name__ == '__main__':
    s = Solution()
    print(s.rotate((
        [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]
        ))) 

    #Output: 
    #   [
    #       [7,4,1], 
    #       [8,5,2],
    #       [9,6,3] 
    #   ]
    
    print(s.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))

    print(s.rotate([[1]]))

