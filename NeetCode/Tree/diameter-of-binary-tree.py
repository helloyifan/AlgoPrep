# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        totalHeight, totalMax= self.helper(root)
        print(totalHeight, totalMax)
        return totalMax
    
    def helper(self, root: Optional[TreeNode]):
        if (root == None):
            return 0, 0
        
        lHeight, lMax = self.helper(root.left)
        rHeight, rMax  = self.helper(root.right)
        
        currHeight = max(lHeight, rHeight ) + 1
        currMax = max(rMax, lMax, rHeight + lHeight)
        
        return currHeight, currMax


'''
[1,2,3,4,5]
[1,2,3]
[-10,9,20,null,null,15,7]
[3]
[-3]
[2, -1]
[1,-2,3]
[-1,null,9,-6,3,null,null,null,-2]
[1,null,2,null,3,null,4,null,5]
'''