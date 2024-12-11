# TC: O(n) we travese through each node
# SC: O(height) for a balanced tree (logN), O(n) in worst case for heap
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if root == None:
                return 0, 0

            lMax, lMaxDiameter = dfs(root.left)
            rMax, rMaxDiameter = dfs(root.right)
            curMaxDiameter = max(lMax + rMax + 1, lMaxDiameter, rMaxDiameter)
            curMaxBranch = max(lMax, rMax) + 1
            return curMaxBranch, curMaxDiameter
        
        maxBranch, maxDiameter = dfs(root)
        print(maxDiameter)
        return maxDiameter-1