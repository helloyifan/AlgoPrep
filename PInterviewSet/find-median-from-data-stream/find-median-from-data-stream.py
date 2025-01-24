# Notes: I was trying to be too clever so took some more tries, see commen for notes
import heapq
class MedianFinder:

    def __init__(self):
        self.leftHeap = [] # maxHeap
        self.rightHeap = [] # minHeap
        return

    def addNum(self, num: int) -> None:
        if len(self.leftHeap) == 0 or num <= self.leftHeap[0] * -1:
            heapq.heappush(self.leftHeap, num * -1)

        # I was trying to be too clever, but this isnt true
        # Its possible for a value to be greater than left side, and lesser than right side
        ##elif len(self.rightHeap) == 0 or num >= self.rightHeap[0]:
        else:
            heapq.heappush(self.rightHeap, num)
        # else:
        #     print("wtf")

        if len(self.leftHeap) > len(self.rightHeap) + 1:
            lPopVal = heapq.heappop(self.leftHeap) * -1
            heapq.heappush(self.rightHeap, lPopVal)

        if len(self.rightHeap) > len(self.leftHeap) + 1:
            rPopVal = heapq.heappop(self.rightHeap)
            heapq.heappush(self.leftHeap, rPopVal * -1)

        return

    def findMedian(self) -> float:
        ret = 0
        if len(self.leftHeap) > len(self.rightHeap):
            ret = self.leftHeap[0] * -1
        elif len(self.rightHeap) > len(self.leftHeap):
            ret = self.rightHeap[0]
        else:
            ret = (( self.leftHeap[0] * -1) +  self.rightHeap[0])/2
        print(ret)
        return ret


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

#sol = MedianFinder()
# sol.addNum(1)
# sol.addNum(2)
# sol.findMedian()
# sol.addNum(3)
# sol.findMedian()

# sol = MedianFinder()
# sol.addNum(-1)
# sol.findMedian()
# sol.addNum(-2)
# sol.findMedian()
# sol.addNum(-3)
# sol.findMedian()
# sol.addNum(-4)
# sol.findMedian()
# sol.addNum(-5)

sol = MedianFinder()
sol.addNum(12)
sol.findMedian()
sol.addNum(10)
sol.findMedian()
sol.addNum(13)
sol.findMedian()
sol.addNum(11)
sol.findMedian()


# if value is smaller then head of leftHeap, add it to leftHeap
#  if left heap size is 2 greater then right heap, then pop one and add to rightHeap
