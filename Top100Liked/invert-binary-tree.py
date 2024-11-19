# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(r):
            if r == None:
                return
            
            # Python has syntatxic sugar r.left, r.right = r.right, r.left
            temp = r.left
            r.left = r.right
            r.right = temp

            dfs(r.left)
            dfs(r.right)
            return
        dfs(root)
        return root