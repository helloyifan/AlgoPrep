# Finished in like 5 mins
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q = []
        if root != None:
            q.append(root)
        ret = []
        while len(q) > 0:
            curLevelRet = []
            tempQ =[]
            while len(q) > 0:
                c = q.pop(0)
                curLevelRet.append(c.val)

                if c.left != None:
                    tempQ.append(c.left)
                if c.right != None:
                    tempQ.append(c.right)

            ret.append(curLevelRet)
            q = tempQ
        return ret

