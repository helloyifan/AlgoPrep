from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        f = 0
        b = len(height) - 1
        maxWater = 0

        while (f < b): # stop when f == b
            minHeight = min(height[f], height[b])
            width = b - f
            curWater = self.calcWater(minHeight, width)
            maxWater = max(maxWater, curWater)
            
            if (height[f] < height[b]):
                f = f+1
            else:
                b = b-1

        return maxWater
    
    def calcWater(self, h: int, w: int) -> int:
        print('h: ', h, 'w', w)
        return h * w

sol = Solution()
height1 = [1,8,6,2,5,4,8,3,7]
r1 = sol.maxArea(height1)
print(r1)

height2 = [1,1]
r2 = sol.maxArea(height2)
print(r2)