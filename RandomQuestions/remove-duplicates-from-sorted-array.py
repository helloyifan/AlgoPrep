from typing import List

# Note:
# if l != r, then that means we should move l+1 = r
    # then we move l up

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l,r = 0,1
        removed = 0
        while r < len(nums):
            if nums[l] != nums[r]:
                print(l+1, nums[l+1])

                nums[l+1] = nums[r]
                removed += 1
                l+=1
            r+= 1


        ret = removed +1
        print('----')
        print(ret, nums)
        return ret

sol = Solution()
sol.removeDuplicates([1,1,2])
sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4])

# 0 ==0 
# 0 != 1