# Time Comp: 
# O(n) - we have to search every node in worse case

# Space COmplexity
# O(m) - stack usage where m is the depth of the tree
# note for balanced BST the its O(logn)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:


        def dfs(r, k, ret):
            if r == None:
                return
            dfs(r.left, k, ret)
            ret.append(r.val)
            if len(ret) == k: # Short circuit this bitch, we dont need to do whole traversal
                return
            dfs(r.right, k, ret)

            return
        ret = []
        dfs(root, k, ret)
        print(ret)
        finRet = ret[k-1] if len(ret) > 0 else 0
        print(finRet) 
        return finRet