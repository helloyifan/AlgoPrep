from typing import List

# How many elements that come after it are just as or shorter

# Brute Froce (17mins)
# Time Complexity:
# For each height, we could check every other neight so its O(n^2)

# Space Complexity:
# We dont use any datastructuress  O(c)

# attempt2largestRectangleArea(15min)
# Too slow
# Time Complexity:
# One pass O(n)
# We are only maintains prev heights that are shorter as they could possibly be the value
# But i guess they could all be shorter so O(n^2)
# We are either maintaing the cur value, or if a prev value was taller (we shorten old value) O(1) in that sense
# Final answer O(n^2)

# Space Complexity:
# I guess if its always shorter then its O(n)
class Solution:
    def bruteForcelargestRectangleArea(self, heights: List[int]) -> int:
        maxRet = 0
        for i, h in enumerate(heights):
            span = 1
            
            # check left
            for ri in range(i-1, -1, -1):
                if heights[ri] < h:
                    break
                else:
                    span +=1
            # check right
            for li in range(i+1, len(heights)):
                if heights[li] < h:
                    break
                else:
                    span +=1
            maxRet = max(maxRet, span*h)
        print(maxRet)
        return maxRet
    
    # Anecdote
    # If the thing you pop, is higher (or just as high), dont put it back in
    # Only put things that are shorter in
    def attempt2largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxHeight = 0
        for h in heights:
            nextStack = []
            alreadyIn = False
            while len(stack) > 0:
                (c, cSpan) = stack.pop(0) #c cur height
                if c < h: # if prev height is shorter
                    nextStack.append((c, cSpan+1))
                    maxHeight = max(maxHeight, c* (cSpan+1))

                elif c >= h:
                    nextStack.append((h, cSpan+1))
                    maxHeight = max(maxHeight, h*(cSpan+1))
                    alreadyIn = True
            
            if not alreadyIn:
                nextStack.append((h,1))
            maxHeight = max(maxHeight, h*1)
            stack = nextStack

        print(maxHeight)
        return  maxHeight

sol = Solution()
sol.largestRectangleArea([7,1,7,2,2,4]) # 8
sol.largestRectangleArea([1,3,7]) # 7