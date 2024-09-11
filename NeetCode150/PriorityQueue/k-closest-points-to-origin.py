from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for p in points:
            euclid = self.generateEuclid(p[0], p[1])
            # if a value is smaller the the largest number in the heap
            # pop off the largest number and add in the samller number

            if len(heap) < k:
                self.maxHeapPush(heap, euclid, p)
            elif self.maxPeak(heap) != None and euclid < self.maxPeak(heap):
                self.maxHeapPop(heap)
                self.maxHeapPush(heap, euclid, p)

        ret = []
        for item in heap:
            ret.append(item[1])
        print(ret)
        return ret
    
    def generateEuclid(self, x, y):
        return (x**2) + (y**2)
    
    def maxPeak(self, heap):
        if len(heap) == 0:
            return None
        
        val = heap[0][0] * -1 
        return val
    
    def maxHeapPush(self, heap, v, cord):
        heapq.heappush(heap, (v * -1, cord))
    
    def maxHeapPop(self, heap):
        ret = heapq.heappop(heap)
        return ret[0] * -1

if __name__ == '__main__':
    sol = Solution()
    sol.kClosest([[0,2],[2,2]], 1)
