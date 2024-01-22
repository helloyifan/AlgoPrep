class Solution():
    def containerWithMostWater(self, nums):
        h, t = 0, len(nums) -1
        maxWater = 0
        while h < t:
            # compute water in current rect 
            lengthOfRect = t - h
            heightOfRect =  min(nums[h], nums[t])
            maxWater = max(maxWater, lengthOfRect * heightOfRect)

            # move h in if nums[h] < nums[t]
            if nums[h] < nums[t]:
                h += 1
            # move t in if nums[t] <= nums[h]
            else:
                t -= 1
        return maxWater


if __name__ == '__main__':
    s = Solution()
    print(s.containerWithMostWater([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(s.containerWithMostWater([1, 1]))