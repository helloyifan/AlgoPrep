

class Solution(object):
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]

        noStart = self.houseRobberOne(nums[1:])
        noEnd = self.houseRobberOne(nums[:-1])

        return max(noStart, noEnd)
    
    def houseRobberOne(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rob1, rob2 = 0, 0
        for num in nums:
            temp = max(rob2 + num, rob1) # you can either rob the next (plus what u had before), or keep what you had
            rob2 = rob1
            rob1 = temp

        return max(rob1, rob2)

if __name__ == '__main__':
    sol = Solution()
    print(sol.rob([2,3,2]))
    print(sol.rob([1,2,3,1]))