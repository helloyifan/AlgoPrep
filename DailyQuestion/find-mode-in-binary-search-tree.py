# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def joinTwoDicts(self, dictA, dictB):
        for i in dictB:
            if (i in dictA):
                dictA[i] += dictB[i]
            else:
                dictA[i] = dictB[i]

    def helper(self, root):
        if (root == None):
            return {}

        dictL = self.helper(root.left)
        dictR = self.helper(root.right)

        self.joinTwoDicts(dictL, dictR)

        if (root.val in dictL):
            dictL[root.val] += 1
        else:
            dictL[root.val] = 1


        return dictL

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        valueCountDict = self.helper(root)

        maxKeyVal =  {"keys": [], "val": float('-inf')}
        for i in valueCountDict:
            if (valueCountDict[i] > maxKeyVal['val'] ):
                maxKeyVal = {"keys": [i], "val": valueCountDict[i]}
            elif(valueCountDict[i] == maxKeyVal['val'] ):
                maxKeyVal["keys"].append(i)
        
        return maxKeyVal['keys']

