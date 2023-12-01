import sys
sys.path.insert(0, '../../Testing')
from ..Testing.ZestyTester import runTests 

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))

## Copy the above only 

s = Solution()
testCases = {
    't1': [[1,2,3,1]],
    't2': [[]]
}

runTests(s.containsDuplicate, testCases)