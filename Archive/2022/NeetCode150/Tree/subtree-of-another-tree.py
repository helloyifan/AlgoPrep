# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if (root == None):
            return False
        
        r = self.checkSameTree(root, subRoot)
        
        if (r == True):
            return True
        
        r1 = self.isSubtree(root.left, subRoot)
        r2 = self.isSubtree(root.right, subRoot)
        
        return r1 or r2
        
        
    
    def checkSameTree(self, root1, root2):
        if (root1 == None and root2 == None):
            return True
        
        if (root1 == None or root2 == None):
            return False
        
        if (root1.val != root2.val):
            return False
        
        r1 = self.checkSameTree(root1.left, root2.left)
        r2 = self.checkSameTree(root1.right, root2.right)
        
        return r1 and r2


'''
[3,4,5,1,2]
[4,1,2]
[3,4,5,1,2,null,null,null,null,0]
[4,1,2]
'''