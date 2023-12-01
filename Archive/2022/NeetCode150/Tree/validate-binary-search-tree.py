# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ret = self.helper(root, float('-inf'), float('inf'))
        print(ret)
        return ret
        
    def helper(self, root, minLim, maxLim):
        
        if (root == None):
            return True
                
        if (root.val >= maxLim or root.val <= minLim):
            return False
        
        l = self.helper(root.left, minLim, root.val)
        r = self.helper(root.right, root.val, maxLim)
        
        return l and r
'''
[2,1,3]
[5,1,4,null,null,3,6]
[2,null,3]
[2]
[5,1,4,6,null,3,null]
[5,4,6,null,null,3,7]
'''