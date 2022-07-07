from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))

## Copy the above only 

s = Solution()

t1 = [1,2,3,1]
s1 = s.containsDuplicate(t1)
print(s1)

t2 = []
s2 = s.containsDuplicate(t2)
print(s2)

t3 = [ b ]