# Notes: Heapq question
# Theres also a quick select solution
# TC: for each element, we are performing a O(log k) operation so O(n * logk)
# SC: At most we are using O(k) space
import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []

        for n in nums:
            if len(h) <= k or n > h[0]:
                heapq.heappush(h, n) #O(logn)
            
            if len(h) > k:
                heapq.heappop(h) #O(logn)
        print(h)
        return h[0]
    
sol = Solution()
sol.findKthLargest([3,2,1,5,6,4], 2)
sol.findKthLargest([3,2,3,1,2,4,5,5,6], 4)
sol.findKthLargest([2,1], 2)