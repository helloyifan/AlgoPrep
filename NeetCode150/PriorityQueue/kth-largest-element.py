import heapq

from typing import List

# If we know k at the start, just make [0] the kths value?
# TOok 15mins got confused

class KthLargest:
    heapNums = None
    sizeOfHeap = None
    def __init__(self, k: int, nums: List[int]):
        self.heapNums = nums
        self.sizeOfHeap = k
        heapq.heapify(self.heapNums)

        for _ in range(len(nums) - k):
            heapq.heappop(self.heapNums)        

    def add(self, val: int) -> int:
        if not self.heapNums or val > self.heapNums[0]:
            heapq.heappush(self.heapNums, val)
        
        if len(self.heapNums) > self.sizeOfHeap:
            heapq.heappop(self.heapNums)

        return self.heapNums[0] if len(self.heapNums) > 0 else None       


if __name__ == "__main__":

    # sol = KthLargest(3, [1,2,3,3])
    # print(sol.add(3)) # 3
    # print(sol.add(5)) # 3
    # print(sol.add(6)) # 3
    # print(sol.add(7)) # 5
    # print(sol.add(8)) # 6
    

    # ["KthLargest", [1, []], "add", [3], "add", [-2], "add", [5], "add", [10], "add", [9]]

    sol = KthLargest(1, [])
    print(sol.add(3)) # 3
    print(sol.add(-2)) # 3
    print(sol.add(5)) # 3
    print(sol.add(10)) # 5
    print(sol.add(9)) # 6
    