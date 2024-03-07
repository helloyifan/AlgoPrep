# Took 22mins
# Working solution
# I don't like this implementation bcuz its confusing
# Basically the tips of the leftHeap (which is a maxHeap) and rightHeap (minHeap)
# Gives you enough to solve the problem
# However, when we add to either the right heap or left heap we have check to see if we should shift a value to the other side
# Because we want to keep left and right side balanced in number of elements
# I dont think my idea of that makes sense and the code is ugly

import heapq

class MedianFinder(object):

    def __init__(self):
        self.leftHeap = []
        self.rightHeap = []
        return

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.rightHeap) == 0 or num > self.rightHeap[0]:
            heapq.heappush(self.rightHeap, num)

            # Shift over from right to left if we have one too many values on right side
            if len(self.rightHeap) > len(self.leftHeap) + 1:
                temp = heapq.heappop(self.rightHeap)
                heapq.heappush(self.leftHeap, temp * -1)
        else: # insert into left side
            heapq.heappush(self.leftHeap, num * -1)
            # shift over from left to right if left has too many values
            if len(self.leftHeap) > len(self.rightHeap) + 1:
                temp = heapq.heappop(self.leftHeap)
                heapq.heappush(self.rightHeap, temp  * -1)
        return
    
    def findMedian(self):

        """
        :rtype: float
        """
        if len(self.rightHeap) > len(self.leftHeap):
            return self.rightHeap[0]
        elif len(self.rightHeap) < len(self.leftHeap):
            return self.leftHeap[0] * -1
        
        return (self.rightHeap[0] + (self.leftHeap[0]*-1)) /2