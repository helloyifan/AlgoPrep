# Notes: Do a binary search like DFS traversal
# TC: O(nums) where we do traverse to every node in the tree once
# SC: O(n) for tree nodes + O(log n) for recursive stack = O(n) total.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root = TreeNode(float('-inf'))
        dummyNode = root

        l, r = 0, len(nums)-1

        def dfs(root, l, r):
            if l > r:
                return
            
            median = (l+r)//2
            medianVal = nums[median]
            curLevelNode = TreeNode(medianVal)
            
            if medianVal < root.val:
                root.left = curLevelNode
            elif medianVal >= root.val:
                root.right = curLevelNode
            
            dfs(curLevelNode, l, median-1)
            dfs(curLevelNode, median+1, r)

        dfs(root, l, r)
        #print(dummyNode.right)
        return dummyNode.right