from typing import List
from collections import defaultdict

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cache = defaultdict(int)

        for i, e in enumerate(arr):
            cache[e] += 1
        
        uniq = {}
        for e in cache:
            key = cache[e]
            if (key in uniq):
                return False
        
            uniq[key] = True
        
        return True

sol = Solution()
arr = [1,2,2,1,1,3]
r1 = sol.uniqueOccurrences(arr)
print(r1)

arr2 = [1,2]
r2 = sol.uniqueOccurrences(arr2)
print(r2)

arr3 = [-3,0,1,-3,1,1,1,-3,10,0]
r3 = sol.uniqueOccurrences(arr3)
print(r3)