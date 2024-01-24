# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        ret = self.helper(p, q)
        return ret

    def helper(self, p, q):
        if p == None and q == None:
            return True
        if p == None or q == None or p.val != q.val:
            return False
        
        l = self.helper(p.left, q.left)
        r = self.helper(p.right, q.right)

        return l and r