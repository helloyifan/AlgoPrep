# Solved in 15mins mostly on instinct

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # helper returns (cur, max)
        def helper(t):
            if t == None:
                return (0, 0)

            l = helper(t.left)
            r = helper(t.right)

            curMax = max(l[0], r[0]) +1 
            childMax = max(l[0] + r[0], l[1], r[1])

            return (curMax, childMax)

        ret = helper(root)

        print(ret)
        return ret[1] # we want the max, not the cur because the cur includes the current incrementer
