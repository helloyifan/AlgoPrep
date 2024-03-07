import heapq

class MedianFinder(object):

    def __init__(self):
        self.heap = []
        return

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.heap, num)     
        return
    
    def findMedian(self):
        """
        :rtype: float
        """
        heapLenIsEven = True if len(self.heap)%2 == 0 else False

        if heapLenIsEven:
            return self.handleEven()

        return self.handleOdd()

    def handleEven(self):
        numOfPops = len(self.heap)//2 + 1

        smallest = None
        secondSmallest = None

        for i in range(0, numOfPops):
            secondSmallest = smallest
            smallest = heapq.heappop(self.heap)

        return (smallest + secondSmallest) / 2
    

    def handleOdd(self):
        numOfPops = len(self.heap)//2 
        smallest = None
        for i in range(0, numOfPops):
            smallest = heapq.heappop(self.heap)
        return smallest
    
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
        
if __name__ == '__main__':
    medianFinder = MedianFinder()
    medianFinder.addNum(1)    #// arr = [1]
    medianFinder.addNum(2)    #// arr = [1, 2]
    print(medianFinder.findMedian()) #// return 1.5 (i.e., (1 + 2) / 2)
    medianFinder.addNum(3)     #// arr[1, 2, 3]
    print(medianFinder.findMedian())  #// return 2.0