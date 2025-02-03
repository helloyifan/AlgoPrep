from typing import List

# Notes: The problem is called 4 sum, but irl we should probably just solve it for k sumx
# One problem detail is that it has to be unique quadruplets, meaning you cant have [2,2,2,2] twice
class Solution():
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort() #O(nlogn)
        
        ret = []
        def kSum(k, nums, decreasingTarget, selected):
            # If k > 2 we handle the recursion
            if k > 2:
                for i in range(len(nums)):
                    if i > 0 and nums[i] == nums[i-1]: # at this level, we cant just use the same value we just used.
                        continue # disregard this iteration keep going

                    selected.append(nums[i])
                    kSum(k-1, nums[i+1:], decreasingTarget - nums[i], selected)
                    selected.pop() # backtracking?
            
            # If k == 2, we can find the last two numbers with l ptr and r ptr
            elif k == 2:
                l, r = 0, len(nums)-1
                while l < r:
                    print(l, r)
                    cur = nums[l] + nums[r]
                    if cur > decreasingTarget:
                        r -= 1
                    elif cur < decreasingTarget:
                        l += 1
                    else: # the cur 2 values hit the target
                        curRet = selected[:]
                        curRet.append(nums[l])
                        curRet.append(nums[r])
                        ret.append(curRet)

                        l += 1
                        # Still move l, after a match, we wanna find rest
                        while l < r and nums[l-1] == nums[l]: # something is wrong with this line
                            l += 1
            else:
                print("invalid edge case")

        kSum(4, nums, target, [])
        print(ret)
        return ret
    

sol = Solution()
#sol.fourSum([8,1,2,3,4,5,6,7], 16)
sol.fourSum([1, 0, -1, 0, -2, 2], 0) # [[-2,-1,1,2], [-2,0,0,2], [-1,0,0,1]]
# sol.fourSum([2,2,2,2,2], 8 ) # [2,2,2,2]