# Notes: Since we have to fill in nums1, lets fill it in from back to front
# becauses the empty spots are at the back
# TC: O(n)
# SC: O(1) as we are doing it in place
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # Since we have to fill in nums1 that has 0 at the back
        # We should start backwards
        h1, h2, = m-1, n-1 
        writeIndex = len(nums1)-1

        while writeIndex >= 0:
            if (h2 <0) or (h1 >= 0 and nums1[h1] > nums2[h2]):
                nums1[writeIndex] = nums1[h1]
                h1 -=1
            elif (h2 >= 0):
                nums1[writeIndex] = nums2[h2]
                h2 -=1
            else:
                raise("Shouldnt happen")
            writeIndex -= 1
        print(nums1)
        return nums1
    
sol = Solution()
sol.merge([1,2,3,0,0,0], 3, [2,5,6], 3)
sol.merge([1], 1, [], 0)
sol.merge([0], 0, [1], 1)
sol.merge([4,5,6,0,0,0], 3, [1,2,3], 3)
