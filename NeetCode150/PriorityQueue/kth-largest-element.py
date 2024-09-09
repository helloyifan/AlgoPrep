import heapq

# If we know k at the start, just make [0] the kths value?
# TOok 15mins got confused

class KthLargest:
    heapNums = None
    sizeOfHeap = None
    def __init__(self, k, nums):
        self.heapNums = nums
        self.sizeOfHeap = k
        heapq.heapify(self.heapNums)

        for _ in range(len(nums) - k):
            heapq.heappop(self.heapNums)

    def add(self, val):
        if val > self.heapNums[0]:
            heapq.heappush(self.heapNums, val)
        
        if len(self.heapNums) > self.sizeOfHeap:
            heapq.heappop(self.heapNums)

        return self.heapNums[0]

if __name__ == "__main__":

    sol = KthLargest(3, [1,2,3,3])
    print(sol.add(3)) # 3
    print(sol.add(5)) # 3
    print(sol.add(6)) # 3
    print(sol.add(7)) # 5
    print(sol.add(8)) # 6
    