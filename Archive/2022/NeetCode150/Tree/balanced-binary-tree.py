
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:       
        validity, height = self.helper(root)
        return validity
        
    def helper(self, root):
        if (root == None):
            return True, 0
        
        rValid, rHeight = self.helper(root.right)
        if (rValid == False):
            return False, 0
        
        lValid, lHeight = self.helper(root.left)
        
        if(lValid == False):
            return False, 0
    
        print(rHeight, lHeight)
        if (abs(rHeight - lHeight) > 1):
            return False, 0 
        
        return True, max(rHeight, lHeight) + 1 

'''
[3,9,20,null,null,15,7]
[1,2,2,3,3,null,null,4,4]
[2,1,3]
[5,1,4,null,null,3,6]
[2,null,3]
[2]
[5,1,4,6,null,3,null]
'''