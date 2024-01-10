# Notes:
# Interesting problem

# Sol:
# The category is BinSearch,
# However logically we arn't exactly performing binary search
# The idea is to basically find the smallest in L, CurVal, R via BinSearch way (so its logn) time

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return float('inf')
        elif len(nums) == 1:
            return nums[0]

        s, e = 0, len(nums) -1
        curIndex = (s + e) // 2
        curVal = nums[curIndex]

        # left
        lVal =self.findMin(nums[s: curIndex])
        # right
        rVal =self.findMin(nums[curIndex + 1:e + 1])

        return min(lVal, curVal, rVal)

if __name__ == '__main__':
    sol = Solution()
    print(sol.findMin( [4,5,6,7,0,1,2]))

    print(sol.findMin( [3,4,5,1,2]))

    print(sol.findMin( [11,13,15,17]))

    print(sol.findMin( [2,1]))
