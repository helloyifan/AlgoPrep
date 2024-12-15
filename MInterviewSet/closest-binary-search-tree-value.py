# Notes:
# I got really confused when dpomg this problem
# Traverse DFS based on relationship to target and root.val
# Keep track of min as we travese down with binary search

# TC: O(logN), sinces its Binary search dfs we only go down one path
# SC: O(h) since this is dfs we use stack, O(n) in the worst case a skewed tree
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        minVal = [root.val]
        def dfs(root):
            if root == None:
                return

            minValDiff = abs(target - minVal[0]) 
            if minValDiff > abs(target - root.val):
                minVal[0] = root.val
            elif minValDiff == abs(target - root.val):
                minVal[0] = min(minVal[0], root.val)

            if target < root.val:
                dfs(root.left)
            else:
                dfs(root.right)
            
            return 
        
        dfs(root)
        print(minVal)
    
        return minVal[0]