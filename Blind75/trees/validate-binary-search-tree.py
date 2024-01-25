# Took 5 mins
# Actually made alot of sense

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        ret = self.helper(root, float('-inf'), float('inf'))
        return ret

    def helper(self, root, minV, maxV):
        if root == None:
            return True

        if minV >= root.val or root.val >= maxV:
            return False

        l = self.helper(root.left, minV, root.val)
        r = self.helper(root.right, root.val, maxV)

        return l and r