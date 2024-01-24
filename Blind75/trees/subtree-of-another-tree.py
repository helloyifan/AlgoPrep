

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        ret = self.findHelper(root, subRoot)
        return ret

    # 1. step through main tree (root) and when the head matches, proceed to 2
    def findHelper(self, root, subRoot):
        if root == None:
            return None
        
        if root.val == subRoot.val:
            ret = self.matchHelper(root, subRoot)
            if ret == True:
                return ret
        
        l = self.findHelper(root.left, subRoot)
        r = self.findHelper(root.right, subRoot)

        return l if l != None else r
    
    # 2. Checks if p and q are the same 
    def matchHelper(self, p, q):
        if p == None and q == None:
            return True
        if p == None or q == None or p.val != q.val:
            return False
        
        l = self.matchHelper(p.left, q.left)
        r = self.matchHelper(p.right, q.right)

        return l and r 