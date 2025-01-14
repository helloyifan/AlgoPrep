# Notes: Weird problem, 
# TC: O(n), we check each element, do dont really swap just replace
# SC: O(1)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ptr = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[ptr] = nums[i]
                ptr += 1
        #print(nums, ptr)
        return ptr