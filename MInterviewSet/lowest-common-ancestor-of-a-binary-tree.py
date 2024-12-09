# Notes: Clean code means to do dfs and return the root when it hits either or
#  We update the root we return when both l and r and nodes and not none
# TC: O(n)
# SC: O(h) WHere h is the height of the tree, However in the worse case it would be O(n)
# Since we use heap memory

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root, p, q):
            if not root:
                return None
            
            if root ==p or root == q:
                return root
            
            l = dfs(root.left, p, q)
            r = dfs(root.right, p, q)

            if l != None and r != None:
                return root
            elif r != None:
                return r
            else:
                return l
        ret = dfs(root, p, q)
        return ret

    def Jonathan_confusing_lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(root, p, q):
            if root == None:
                return False, False, None
            
            pFound, qFound = False, False
            if root == p:
                pFound = True
            
            if root == q:
                qFound = True
            
            
            lPFound, lQFound, lNode = dfs(root.left, p, q)
            if lPFound and lQFound:
                return True, True, lNode

            rPFound, rQFound, rNode = dfs(root.right, p, q)
            if rPFound and rQFound:
                return True, True, rNode

            pFound = pFound or lPFound or rPFound
            qFound = qFound or lQFound or rQFound
            if pFound and qFound:
                return True, True, root

            return pFound, qFound, None

        pFound, qFound, ret = dfs(root, p, q)
        return ret