from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l, r = 0, 0 
        runningSum = 0
        retTotal = 0
        while r < len(nums):
            runningSum += nums[r]
            r+=1
            while l < r and runningSum >= k/(r-l):
                #runningSum -= nums[l]
                l += 1
                runningSum = 0
                r = l

            if runningSum != 0 and runningSum < k/(r-l):
                #print(runningSum, k/(r-l+1))
                retTotal += 1


        print(retTotal)
        return retTotal

sol = Solution()
sol.countSubarrays([2,1,4,3,5], 10) # 6
sol.countSubarrays([1,1,1], 5) # 5
sol.countSubarrays([1,2,9,1,5],96) # 15


# 2 adjustedK = 10/1
# 2,1 adjustedK = 10/2
# 2,1,4 adjustedK = 10/3 

# So the opersation is that adjustedK keeps getting smaller and smaller
# if runningSum is always getting bigger and adjusted k is getting smaller
# then give up, move the LHS
