# Time Complexity
# Add O(1)
# Count
# O(n) for each node in the matrix
# once a node is found, we do two O(1) checks
# count runtime is O(n)

# Space COmplexity
# O(n) things will be added
from typing import List
from collections import defaultdict

class DetectSquares:

    def __init__(self):
        self.sparceMatrix = defaultdict(lambda: defaultdict(int))
        return

    def add(self, point: List[int]) -> None:
        r, c = point[0], point[1]
        self.sparceMatrix[r][c] += 1
        return

    def count(self, point: List[int]) -> int:

        p1 = point
        ret = 0
        for r in self.sparceMatrix.keys():
            if r == p1[0]:
                continue
            for c in self.sparceMatrix[r].keys():
                if c == p1[1]:
                    continue
                
                # Time sink here, this is what a square is 
                # hor len must be equal to ver len to continue
                if abs(r - p1[0]) != abs(c - p1[1]): 
                    continue

                p2 = [r, c]
                p2Val = self.sparceMatrix[r][c]

                cond, maxOfP3P4 = self.findNonDiagonalPoints(p1, p2)
                if cond == True:
                    # print(p1, p2, p2Val)
                    ret += maxOfP3P4 * p2Val

        return ret
    

    def findNonDiagonalPoints(self, p1, p2):
        p3 = [p1[0], p2[1]]
        p4 = [p2[0], p1[1]]

        if p3[0] in self.sparceMatrix:
            if p3[1] in self.sparceMatrix[p3[0]]:
                if p4[0] in self.sparceMatrix:
                    if p4[1] in self.sparceMatrix[p4[0]]:
                        pointsOnP3 = self.sparceMatrix[p3[0]][p3[1]]
                        pointsOnP4 = self.sparceMatrix[p4[0]][p4[1]]
                        #print(p3, pointsOnP3, p4, pointsOnP4)
                        return True, pointsOnP3 * pointsOnP4
        return False, 0

# Your DetectSquares object will be instantiated and called as such:
obj = DetectSquares()
# obj.add([3,10])
# obj.add([11,2])
# obj.add([3,2])
# print(obj.count([11,10]))
# print(obj.count([14,8]))
# obj.add([11,2])
# print(obj.count([11,10]))


# Test 2

# obj.add([3, 3])
# obj.add([6, 3])
# obj.add([3, 6])
# print(obj.count([6, 6]))
# obj.add([2, 2])
# obj.add([6, 2])
# obj.add([2, 6])
# print(obj.count([6, 6]))
# obj.add([2, 2])
# obj.add([3, 3])
# print(obj.count([6, 6]))
# obj.add([6, 3])
# obj.add([3, 6])
# print(obj.count([6, 6]))
# 1, 2, 4, 10

# Test 3

# obj.add([5, 5])
# obj.add([5, 6])
# obj.add([6, 5])
# obj.add([6, 6])
# print(obj.count([7, 7]))
# print(obj.count([5, 5]))


# Test 4

obj.add([5, 10])
obj.add([10, 5])
obj.add([10, 10])
print(obj.count([5, 5]))
obj.add([3, 0])
obj.add([8, 0])
obj.add([8, 5])
print(obj.count([3, 5]))
obj.add([9, 0])
obj.add([9, 8])
obj.add([1, 8])
print(obj.count([1, 0]))
obj.add([0, 0])
obj.add([8, 0])
obj.add([8, 8])
print(obj.count([0, 8])) #should be 2
