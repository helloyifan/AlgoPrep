# Note: Deque .appendleft() to insert to front in constant time
# .pop() to remove from back

# TC: O(1) for both init and next
# SC: O(size) 

class MovingAverage:

    def __init__(self, size: int):
        self.runningSum = 0
        self.size = size
        self.dq = deque([])

    def next(self, val: int) -> float:
        self.dq.appendleft(val)
        self.runningSum += val

        if len(self.dq) > self.size:
            removedVal = self.dq.pop()
            self.runningSum -= removedVal
        
        return self.runningSum/len(self.dq)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)