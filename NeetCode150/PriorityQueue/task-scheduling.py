import heapq

from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        lastOccurance = {}
        heap = []

        for i, t in enumerate(tasks):
            heapq.heappush()
        return

if __name__ == '__main__':
    sol = Solution()

    sol.leastInterval(["X","X","Y","Y"], 2) # 5
    sol.leastInterval(["A","A","A","B","C"], 3) # 9
