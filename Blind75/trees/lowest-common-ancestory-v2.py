# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Runtime complexity
# 

class Solution:
    def lowestCommonAncestorOfBinaryTree(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def dfs(root, p, q):
            if p.val <= root.val <= q.val:
                return root

            ret = None
            if p.val < root.val and q.val < root.val:
                root = dfs(root.left, p, q)
            elif p.val > root.val and q.val > root.val:
                root = dfs(root.right, p, q)
            return root

        ret = dfs(root,p ,q)
        print(ret)
        return ret
    
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def dfs(root, p, q):

            if root == None:
                return None 
            
            if root.val == p.val:
                return root
            
            if root.val == q.val:
                return root
            
            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q)

            if left and right:
                return root

            return left if left else right

        ret = dfs(root,p ,q)
        print(ret)
        return ret
        