# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        self.pPath = []
        self.lca = None
        self.helper(root, p.val, False)
        self.helper(root, q.val, True)

        ret = self.lca
        return ret
    
    def helper(self, root, t, matchMode):
        if root == None:
            return False

        if root.val == t:
            if matchMode == False:
                self.pPath.append(root.val)
            return True        

        l = self.helper(root.left, t, matchMode)
        r = self.helper(root.right, t, matchMode)

        if l == True or r == True:
            if matchMode == False:
                self.pPath.append(root.val)
            else: # MatchMode == true
                if root.val in self.pPath and self.lca == None:
                    self.lca = root
                return True # Returning here intended as short circuit

            return True
        else:
            return False