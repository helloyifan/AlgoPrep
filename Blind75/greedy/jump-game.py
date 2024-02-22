# Took 5 min, did good

# The question allows you to jump as far as you want (top limit being the value)
# The main part is  max(maxDist, i + e)
# Which means, we want to figure out at index i, do we go further if we were to jump at index i or if we jumped further before
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxDist = 0 # 
        for i, e in enumerate(nums):
            if maxDist < i:
                return False
            
            maxDist = max(maxDist, i + e)
        
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.canJump([2,3,1,1,4]))
    print(s.canJump([3,2,1,0,4]))