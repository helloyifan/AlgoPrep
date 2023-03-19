# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pHistory = self.helper(root, p)
        qHistory = self.helper(root, q)
        
        # print(pHistory)
        # print(qHistory)

        matchVal = self.findFirstElemInBothList(pHistory, qHistory)
        # print(matchVal)

        return self.digUpNode(root, matchVal)


    def digUpNode(self, root, key):
        if (root == None):
            return None
        
        if (root.val == key):
            return root

        l = self.digUpNode(root.left, key)
        if (l != None):
            return l
        r = self.digUpNode(root.right, key)
        if (r != None):
            return r

        return None


    def helper(self, root, target):
        if (root == None):
            return None

        if (root == target):
            return [root.val]

        lRet = self.helper(root.left, target)
        rRet = self.helper(root.right, target)

        if (lRet != None):
            lRet.append(root.val)
            return lRet

        if (rRet != None):
            rRet.append(root.val)
            return rRet

        return None

    def findFirstElemInBothList(self, pList, qList):
        for p in pList:
            if (p in qList):
                return p        
        return None