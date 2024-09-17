# Solved in 7mins from intuition

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def helper(r, maxValSoFar):
            if r == None:
                return 0 # If this is or is not good
            
            maxValNow = max(r.val, maxValSoFar)

            left = helper(r.left, maxValNow)
            right = helper(r.right, maxValNow)

            ret = 0

            # current
            if maxValSoFar <= r.val: #or <=
                ret += 1

            ret += left
            ret += right
            return ret

        ret = helper(root, float('-inf'))
        print(ret)
        return ret