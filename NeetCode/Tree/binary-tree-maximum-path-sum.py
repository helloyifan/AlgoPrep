# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        pathVal, maxVal = self.helper(root)
        # return max(pathVal, maxVal)
        return  maxVal
        
    def helper(self, root: Optional[TreeNode]):
        if (root == None):
            return 0, 0
        
        
        lPathVal, lMax = None, None
        rPathVal, rMax = None, None
        
        if (root.left == None):
            lPathVal, lMax = 0, float('-inf')
        else:
            lPathVal, lMax = self.helper(root.left)

        if (root.right == None):
            rPathVal, rMax = 0, float('-inf')
        else:    
            rPathVal, rMax = self.helper(root.right)
        
        curMax = max(lMax, rMax, lPathVal + rPathVal + root.val)
        curPathVal = max(lPathVal, rPathVal) + root.val
        
        return curPathVal, curMax
        
s = Solution()

## Dumb ass test cases

# [1,2,3]
# [-10,9,20,null,null,15,7]
# [3]
# [-3]
# [2, -1]