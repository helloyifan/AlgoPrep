# Notes: Old add at leaf node, leaf node has l = None and r = none
# TC: O(n) - Staightforwards dfs
# SC: For callstack  O(height) where height = logN for balanced tree , otherwise O(n) in skewed tree - O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, runningSum):
            if root == None:
                # Don't return runningSum here because
                # We arnt sure if its just branch thats non or if parent was leaf node
                return 0 

            currentLevelSum = (runningSum * 10) + root.val

            totalSum = 0

            # Note we only want to include the sum if its at root
            if root.left == None and root.right == None:
                totalSum += currentLevelSum 
            else:
                totalSum += dfs(root.left, currentLevelSum) 
                totalSum += dfs(root.right, currentLevelSum)
                    
            return totalSum
        
        ret = dfs(root, 0)
        print(ret)
        return ret