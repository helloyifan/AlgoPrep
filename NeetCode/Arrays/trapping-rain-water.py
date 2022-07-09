from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        lengthOfInput = len(height)
        maxLeftToRight = [None] * lengthOfInput
        maxRightToLeft = [None] * lengthOfInput

        max1 = 0
        for i in range(0, lengthOfInput):
            max1 = max(max1, height[i])
            maxLeftToRight[i] = max1
        max2 = 0
        # Fking backwards for loops have to be weird
        for j in range(lengthOfInput-1, -1, -1):
            max2 = max(max2, height[j])
            maxRightToLeft[j] = max2

        # print(maxLeftToRight)
        # print(maxRightToLeft)
        
        rainWater = 0

        for k in range(0, lengthOfInput):
            curWater = min(maxLeftToRight[k], maxRightToLeft[k]) - height[k]
            #print(curWater)
            rainWater += curWater

        return rainWater


s = Solution()

height = [0,1,0,2,1,0,1,3,2,1,2,1]
r1 =  s.trap(height)
print(r1)

height2 = [4,2,0,3,2,5]
r2 =  s.trap(height2)
print(r2)

height3 = [1]
r3 =  s.trap(height3)
print(r3)