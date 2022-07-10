import heapq
from typing import List

# This is an interesting problem
# Q: So how do you get the kth largest from the min heap?
# A: well basically just keep a min heap of elements that consists of the kth largest and larger elements

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.h = nums
        heapq.heapify(self.h) # since heapify does it inplace

        self.k = k 
        
        # Remove everything except for the kth largest, and larger numbers
        while (len(self.h) > self.k):
            heapq.heappop(self.h)
        
        return None

    def add(self, val: int) -> int:
        heapq.heappush(self.h, val)
    
        if (len(self.h) > self.k):
            heapq.heappop(self.h)

        return self.h[0] 

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)



'''
First list, function name
Second list, function parameter

["KthLargest","add","add","add","add","add"]
[[3,[4,5,8,2]],[3],[5],[10],[9],[4]]

["KthLargest","add","add","add","add","add"]
[[1,[]],[-3],[-2],[-4],[0],[4]]
'''