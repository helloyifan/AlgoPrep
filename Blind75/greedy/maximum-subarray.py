# Under 5 mins when i remember the Kadane's algorithm
# This is like Kadane's algorithm
# The jist of it, we do running sum until the number is negative, 
# then we start counting again at the new index 
# (if the prev sum was negative, then we no longer consider it)

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxVal = float('-inf')
        runningSum = 0

        for num in nums:
            runningSum += num
            maxVal = max(maxVal, runningSum)

            if runningSum < 0:
                runningSum = 0

        return maxVal

if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print(s.maxSubArray([1]))
    print(s.maxSubArray([5,4,-1,7,8]))
    