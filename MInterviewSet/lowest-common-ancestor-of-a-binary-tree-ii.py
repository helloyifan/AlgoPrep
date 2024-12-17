'''
Notes:
Pseudo-code for LCA with nulls

## Base Case:
If the current node is null, return (null, false, false).

## Search Left and Right:
Recursively find the LCA in the left and right subtrees.

## Current Node Check:

If the current node is p or q, mark it as found.

LCA Conditions:
If both sides return an LCA, the current node is the LCA.

If the current node matches p or q and the other node is found in a subtree, the current node is the LCA.

Propagate Results:

Return the LCA from the left or right subtree if it exists.

## Final Step:
At the root, if both p and q are found, return the LCA. Otherwise, return null.
'''

# TC: O(n) to traverse every node of a Binary Tree
# SC: O(height) if this is a balanced tree because we use call stack (height = log number of nodes), 
# if this is a skewed tree space is O(n)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(root, p, q):
            if root == None:
                return None, None, None #LCA, pFound, qFound

            rLCA, rPFound, rQFound = dfs(root.right, p, q)
            lLCA, lPFound, lQFound = dfs(root.left, p, q)

            curPFound, curQFound = root == p, root == q

            # If L and R are found
            if rLCA != None and lLCA != None:
                return root, True, True

            # If Cur is LCA and either p or q are found
            if curPFound and (rQFound or lQFound):
                return root, True, True
            if curQFound and (rPFound or lPFound):
                return root, True, True
            
            # If we found P or Q return it up
            if curPFound:
                return root, True, False
            if curQFound:
                return root, False, True

            # Propage results of right exists
            if rLCA != None:
                return rLCA, rPFound, rQFound
            
            # Propagate result if left exiists
            if lLCA != None:
                return lLCA, lPFound, lQFound

            return None, None, None

        lca, pFound, qFound = dfs(root, p, q)

        ret = None
        if pFound and qFound:
            ret = lca
        return ret