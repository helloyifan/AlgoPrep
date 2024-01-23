class Solution():
    def houseRobber(self, nums):
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(n + rob1, rob2) # whats bigger, robbing current house or taking what we had before (non adjacent before)
            rob1 = rob2
            rob2 = temp
        return rob2

if __name__== '__main__':
    s = Solution()
    print(s.houseRobber([1,2,3,1])) # 1 + 3 = 4
    print(s.houseRobber([2,7,9,3,1])) # 2 + 9 + 1 = 12
    print(s.houseRobber([1,2,100,3,4,5,6])) # 1,100,4,6
    print(s.houseRobber([1,2,100,3,4,100,6])) # 1,100,100