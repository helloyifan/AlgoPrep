# Took 5 min
# Actually makes logical sense if you think about it

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        self.inorderTraversal(root)
        ret = self.ret
        return ret

    def inorderTraversal(self, root):
        if root == None:
            return

        self.inorderTraversal(root.left)

        # Special part, decrement the object level counter
        self.k -= 1
        if self.k == 0:
            self.ret = root.val
            return

        self.inorderTraversal(root.right)

        return