# Note you can also do this question with heapq heapq.heappush But heappush is O(n) and we could be pushing every element so its O(nlogk) 
    # Where k is the number of unique elements
# TC: O(n) for inital aggregation, O(nlogn) for the sort and O(k) for the final result = O(nlogn)
# SC: O(n) for the defeault dict worse case everything can go in it
from typing import List
from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dd = defaultdict(int)

        for n in nums:
            dd[n] +=1
        
        sortedFlipedDict = sorted(dd.items(), key=lambda x : -x[1]) # - to sort desending, x[1] to sort by val of dict

        ret = []
        for n in range(k):
            ret.append(sortedFlipedDict[n][0])

        print(ret)
        return ret

    def heap_topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dd = defaultdict(int)

        for n in nums:
            dd[n] +=1
        
        h = []
        for key in dd:
            heapq.heappush(h, (-dd[key], key))

        ret = []
        for n in range(k):
            temp = heapq.heappop(h)
            ret.append(temp[1])

        print(ret)
        return ret
sol = Solution()
sol.topKFrequent( [1,1,1,2,2,3], 2) #[1,2]

sol.topKFrequent( [1], 1) #[1]
sol.topKFrequent( [1, 2], 2) #[1]
