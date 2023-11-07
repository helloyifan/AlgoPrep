import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # negative values for max heap
        maxHeapUtil.maxHeapify(stones) 

        while len(stones) > 1:
            a = maxHeapUtil.maxheappop(stones)
            b = maxHeapUtil.maxheappop(stones)
            ret = a-b if a > b  else b-a            
            maxHeapUtil.maxheappush(stones, ret)

        return maxHeapUtil.maxheappop(stones)

class maxHeapUtil:
    def maxHeapify(lst):
        for i in range(0, len(lst)):
            lst[i] = lst[i] * -1
        heapq.heapify(lst)

    def maxheappush(heap, item):
        heapq.heappush(heap, item * -1)

    def maxheappop(heap):
        return heapq.heappop(heap) * -1


"""
[2,7,4,1,8,1]
[1]
[1,1,1,1,1,1,1,2,3,4,5,6,7]
"""

s = Solution()
t = [2,7,4,1,8,1]
r = s.lastStoneWeight(t)
print(r)

t2 = [1]
r2 = s.lastStoneWeight(t2)
print(r2)