# Solved in 7mins from intuition

# Time complexity:
# O(n) DFS traversal, we process each node once
# Space complexity:
# O(n) Worst case is that every node ends up in the stack

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(r, maxValSoFar):
            if r == None:
                return 0 # If this is or is not good
            
            maxValNow = max(r.val, maxValSoFar)

            left = dfs(r.left, maxValNow)
            right = dfs(r.right, maxValNow)

            ret = 0

            # current
            if maxValSoFar <= r.val: #or <=
                ret += 1

            ret += left
            ret += right
            return ret

        ret = dfs(root, float('-inf'))
        print(ret)
        return ret