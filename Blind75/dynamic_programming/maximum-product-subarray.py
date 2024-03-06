# Took 30 mins
# Not really sure how its a dp question
# BUt its a very interesting question to think about 
# Should redoo
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxV, minV = nums[0], nums[0]

        ret = nums[0]

        for i, num in enumerate(nums[1:]):
            curMaxV = maxV * num            
            curMinV = minV * num

            maxV = max(curMaxV, curMinV, num)
            minV = min(curMaxV, curMinV, num)
            
            ret = max(ret, maxV)
        return ret

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProduct([2,3,-2,4]))
    print(sol.maxProduct([-2,0,-1]))
    print(sol.maxProduct([2,3,-2,4,10]))
    print(sol.maxProduct([-2]))
    print(sol.maxProduct([2,-5,-2,-4,3])) #24


