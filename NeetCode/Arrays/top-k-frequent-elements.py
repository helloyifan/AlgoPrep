from typing import List
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(lambda: 0) # defaultdict takes a function (default_factory) for what it should return
        for i, e in enumerate(nums):
            d[e] += 1

        sortedD = sorted(d.items(), key=lambda x: x[1]) # d.items give (key:val) in a set, sort by second item in set
        retD = sortedD[len(sortedD)-k:] # Trim last k elements 

        ret = []
        for key, val in retD: #retD is a list of tuples
            ret.append(key)
        return ret

sol = Solution()

nums = [1,1,1,2,2,2,2,2,3,4,4,4,4,4]
k = 2
print(sol.topKFrequent(nums, k))

nums1 = [1]
k1 = 1
print(sol.topKFrequent(nums1, k1))