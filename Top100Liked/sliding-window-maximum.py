
# Intuition for the problem: (Not solved optimally)
# Double ended queue (bcuz with deque popleft is O(1) where with a list.pop(0) is O(n))
# We want to maintain a "Monotonically Decreasing Queue" (Monotonic Queue)
# A queue thats always decreasing [4, 3, ,2 ,1]

# The head value will be the max val of the subarray
# Just maintain the deque such that is always the case with the below 3 rules
# Rule 1. When you get a new value, pop from R to L until the last value in the deque is bigger than new value or deque is empty
# Rule 2. If a value is out of the window, pop it from the L (front)
# Rule 3. add the new value

# Time Complexity
# O(n) for outer loop,
# Internal for Loop would will only process each index once,
# In total its O(n)

# Space Complexity
# O(n) for the dequeue

from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        doublyEndedQueue = deque() # (index, val) #[0]: is for the index of num, [1], is val num

        ret = []
        for i, n in enumerate(nums):
            # Rule 1.
            while len(doublyEndedQueue) > 0  and doublyEndedQueue[len(doublyEndedQueue)-1][1] < n:
                doublyEndedQueue.pop()
            # Rule 2
            if len(doublyEndedQueue) > 0  and i >= doublyEndedQueue[0][0] + k:
                doublyEndedQueue.popleft()
            # Rule 3
            doublyEndedQueue.append((i,n))

            if i >= k-1: # Dont build ret until we have k length 
                ret.append(doublyEndedQueue[0][1]) #the head value is the max 

        print(ret)
        return ret
  
sol = Solution()
sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) # [3,3,5,5,6,7]
sol.maxSlidingWindow([1,3,1,2,0,5], 3) # [3,3,2,5]
sol.maxSlidingWindow([7,2,4], 2) # [7, 4]
sol.maxSlidingWindow([-7,-8,7,5,7,1,6,0], 4) #[7,7,7,7,7]