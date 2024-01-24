# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        ret = self.helper(root)
        return ret
    
    def helper(self, root):
        if root == None:
            return 0
        l = self.helper(root.left)
        r = self.helper(root.right)
        return max(l, r) + 1