# Probably took 30mins in total, 
# But like i didn't lean anything it was just alot of edgecase
# Like its possible for one node to be the answe
# But its also possible for lSum + rSum + root.val

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxSum, curSum = self.helper(root)
        print(maxSum, curSum)
        return maxSum

    def helper(self, root):
        if root == None:
            return float('-inf'), float('-inf') # (max sum, branch sum)

        lMaxSum, lSum = self.helper(root.left)
        rMaxSum, rSum  = self.helper(root.right)
        
        curSum = root.val + max(lSum, rSum, 0) # 0 incase that left and right side are both negative
        curMaxSum = max(curSum, lSum + rSum + root.val, lMaxSum, rMaxSum)

        return  curMaxSum, curSum 

