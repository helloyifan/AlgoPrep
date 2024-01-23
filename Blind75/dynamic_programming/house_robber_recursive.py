class Solution():
    def houseRobber(self, nums):
        dp = {}
        ret = self.helper(nums, 0)
        return ret
    
    def helper(self, nums, sum):
        if len(nums) == 0:
            return sum

        r1 = self.helper(nums[1:], sum)
        r2 = 0
        if len(nums) > 1:
            r2 = self.helper(nums[2:], sum + nums[0])

        return max(r1, r2)
    
if __name__== '__main__':
    s = Solution()
    print(s.houseRobber([1,2,3,1])) # 1 + 3 = 4
    print(s.houseRobber([2,7,9,3,1])) # 2 + 9 + 1 = 12
    print(s.houseRobber([1,2,100,3,4,5,6])) # 1,100,4,6
    print(s.houseRobber([1,2,100,3,4,100,6])) # 1,100,100