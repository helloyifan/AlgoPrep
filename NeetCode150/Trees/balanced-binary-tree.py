# Took 5 mins, just by instinct

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def helper(t):
            if t == None:
                return 0, True # maxHeight, isBalanced
        
            l, lBalanced = helper(t.left)
            r, rBalanced = helper(t.right)
            
            curBalanced = True
            if not lBalanced or not rBalanced or abs(l-r) > 1:
                curBalanced = False


            return max(l,r) + 1, curBalanced

        maxHeight, isBalanced = helper(root)
        return isBalanced