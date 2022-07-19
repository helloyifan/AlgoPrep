# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p == None and q == None):
            return True
        elif(p == None or q == None):
            return False
        elif (p.val != q.val):
            return False
        
        l = self.isSameTree(p.left, q.left)
        r = self.isSameTree(p.right, q.right)
        
        return l and r

'''
[1,2,3]
[1,2,3]
[1,2]
[1, null, 2]
[1,2,1]
[1,1,2]
[5,1,4,null,null,3,6]
[5,1,4,null,null,3,6]
[2,null,3]
[2,null,3]
[2]
[1]
[5,1,4,6,null,3,null]
[5,4,6,null,null,3,7]
'''