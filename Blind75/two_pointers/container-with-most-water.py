class Solution():
    def containerWithMostWater(self, nums):
        # Left to right
        leftToRightWater = [None] * len(nums)
        for i, num in enumerate(nums):
            if i == 0:
                continue
            prevI = i - 1
            prevNum = nums[prevI]
            leftToRightWater[i] = prevNum - num
        print(leftToRightWater)
        return


if __name__ == '__main__':
    s = Solution()
    s.containerWithMostWater([1, 8, 6, 2, 5, 4, 8, 3, 7])