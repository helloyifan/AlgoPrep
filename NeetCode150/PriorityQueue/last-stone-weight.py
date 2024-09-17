from typing import List
import heapq

# Took 7 mins, all intuition, it was fun
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        for s in stones:
            self.maxHeapPush(h, s)
        
        while len(h) > 1:
            s1 = self.maxHeapPop(h)
            s2 = self.maxHeapPop(h)

            newVal = abs(s1 - s2)
            if newVal > 0:
                self.maxHeapPush(h, newVal)

        ret = 0
        if len(h) == 1:
            ret = self.maxHeapPeak(h)
        print(ret)
        return ret
    
    def maxHeapPush(self, h, v):
        heapq.heappush(h, v * -1)
        return
    
    def maxHeapPop(self, h):
        return heapq.heappop(h) * -1
    
    def maxHeapPeak(self, h):
        return h[0] * -1
    

if __name__ == '__main__':
    sol = Solution()
    sol.lastStoneWeight([2,3,6,2,4]) # 1
    sol.lastStoneWeight([1,2]) # 1
    sol.lastStoneWeight([2,2]) # 0
    