class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        leftSideMax = self.computeLeftToRight(height)
        #print(leftSideMax)

        rightSideMax = self.computeRightToleft(height)
        #print(rightSideMax)

        return self.computeWaterSum(leftSideMax, rightSideMax, height)

    # compute left to right
    def computeLeftToRight(self, height):
        leftSideMax = []
        prevMax = 0
        for i in height:
            prevMax = max(prevMax, i)
            leftSideMax.append(prevMax)

        return leftSideMax

    def computeRightToleft(self,height):
        rightSideMax = []
        prevMax = 0
        for i in range(len(height)-1, -1 ,-1):
            prevMax = max(prevMax, height[i])
            rightSideMax.insert(0,prevMax)

        return rightSideMax

    def computeWaterSum(self, l2r, r2l, height):
        length = len(height)
        ret = 0 
        for i in range(0, length):
            waterAtIndex= min(l2r[i], r2l[i]) - height[i]
            if waterAtIndex > 0:
                ret += waterAtIndex
        return ret

if __name__  == '__main__':
    
    sol = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(sol.trap(height))

    height2 = [4,2,0,3,2,5]
    print(sol.trap(height2))


##
# lSideMax = [0,1,1,2,2,2,2,3,3,3,3]  
# rSideMax = [3,3,3,3,3,3,3,2,2,2,1]
# asdasdas = [0,1,0,2,1,0,1,3,2,1,2,1]

# min of lSideMax, rSideMax, and height
# vals  = 0,0,1,0,1,2,1 