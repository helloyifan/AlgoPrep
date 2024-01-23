# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.helper(root)
        return root

    def helper(self, root):
        if root == None:
            return None
        
        l = self.helper(root.left)
        r = self.helper(root.right)
        root.left = r
        root.right = l
        return root