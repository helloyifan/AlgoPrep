import heapq
class MedianFinder:

    def __init__(self):
        leftHeap = [] # maxHeap
        rightHeap = [] # minHeap
        return

    def addNum(self, num: int) -> None:
        return

    def findMedian(self) -> float:
        return        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

sol = MedianFinder()
sol.addNum(1)
sol.addNum(2)
sol.findMedian()
sol.addNum(3)
sol.findMedian()


# if value is smaller then head of leftHeap, add it to leftHeap
#  if left heap size is 2 greater then right heap, then pop one and add to rightHeap
