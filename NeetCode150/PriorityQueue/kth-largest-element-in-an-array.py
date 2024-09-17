from typing import List
import heapq

# Heapq solution in 6 min, but not the best solution
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for i in nums:
            heapq.heappush(h, i * -1)

        ret = None
        for _ in range(k):
            ret = heapq.heappop(h) * -1
        
        print(ret)
        return ret
    
if __name__ == '__main__':
    sol = Solution()

    sol.findKthLargest([2,3,1,5,4], 2) #4
    sol.findKthLargest([2,3,1,1,5,5,4], 3) #4
    