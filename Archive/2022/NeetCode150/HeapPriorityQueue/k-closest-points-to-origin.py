from queue import PriorityQueue
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        q = PriorityQueue()

        for i, point in enumerate(points):
            dis = self.euclideanDistanceWithSqrt(point)
            q.put((dis, point))

        pops = []
        for i in range(0, k): #1 <= k <= points.length <= 104, So idc lol 
            pops.append(q.get()[1])

        return pops


    def euclideanDistanceWithSqrt(self, point: List[int]):
        return point[0] * point[0] + point[1] * point[1]

s = Solution()

points = [[1,3],[-2,2]]
k = 1
r = s.kClosest(points, k)
print(r)

points2 = [[3,3],[5,-1],[-2,4]]
k2 = 2
r2 = s.kClosest(points2, k2)
print(r2)