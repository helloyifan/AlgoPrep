# Notes: Question wants inclusive between low and high
# TC: O(n) in the worst case we can traverse the whole tree
# SC: O(nd) given we are using a BST we cant assume its balanced
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def dfs(root, low, high):
            if root == None:
                return 0
            
            curVal = 0
            if low <= root.val <= high: #Note its inclusive
                curVal += root.val

            if low < root.val:
                curVal += dfs(root.left, low, high)
            
            if root.val < high:
                curVal += dfs(root.right, low, high)
            
            return curVal
        
        ret = dfs(root, low, high)
        return ret