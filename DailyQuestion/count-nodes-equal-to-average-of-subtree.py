# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    emptyRet = {"sum": 0, "count": 0, "ret": 0} 

    def helper(self, root):
        if (root == None):
            return self.emptyRet.copy()
        
        if (root.left != None):
            lItem = self.helper(root.left)
        else:
            lItem = self.emptyRet.copy()

   
        if (root.right != None):
            rItem = self.helper(root.right)
        else:
            rItem = self.emptyRet.copy()


        newSum = lItem['sum'] + rItem['sum'] + root.val
        newCount = lItem['count'] + rItem['count'] + 1
        newRet = lItem['ret'] + rItem['ret']

        if (newSum//newCount == root.val): #// is round down divison
            newRet += 1

        return {"sum": newSum, "count": newCount, "ret": newRet}



    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        finalItem = self.helper(root)

        return finalItem["ret"]