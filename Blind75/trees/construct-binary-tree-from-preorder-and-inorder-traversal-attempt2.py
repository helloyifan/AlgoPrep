# Spent 25 min and got stuck, netval isnt the correct concept


# Hint for attempt 3 is the relationship the index or curVal inorder. and that same index in preorderr

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        root = self.helper(preorder, inorder)
        return root
    
    def helper(self, preorder, inorder):
        if len(preorder) == 0:
            return None

        curVal = preorder[0]
        curNode = TreeNode(curVal)

        curValPreOrderIndex = preorder.index(curVal)
        curValInOrderIndex = inorder.index(curVal)

        nextVal = 1 # This next val mechanism isnt right,
        # it needs to be something that can figure out where the left and right is in preorder
        if curValInOrderIndex - 1 >= 0:
            l = self.helper(preorder[nextVal:], inorder[:curValInOrderIndex])
            curNode.left = l
            # nextVal += 1
        
        if curValInOrderIndex + 1 < len(inorder):
            r = self.helper(preorder[nextVal:], inorder[curValInOrderIndex + 1:])
            curNode.right = r
        
        return curNode

if __name__ == '__main__':
    s = Solution()
    # print(s.buildTree([3,9,20,15,7],[9,3,15,20,7]))
    # print(s.buildTree([1,2],[1,2]))
    print(s.buildTree([3,1,2,4], [1,2,3,4]))