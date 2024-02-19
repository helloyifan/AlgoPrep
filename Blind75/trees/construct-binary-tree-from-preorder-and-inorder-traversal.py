# Took 15mins
# The essence of this question is the relationship between preorder and inorder array indexes
# The location (lets call this value mid) of the first preorder value in the inorder array, means something to the preorder array
# What it means is thatelements to the left of mid are children of first preorder value
# Chatgpt: So, to answer your question, yes, all values left of mid in the preorder traversal are the values of the children of the current root node.

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
        if len(preorder) <= 0:
            return None
        
        curVal = preorder[0]
        curNode = TreeNode(curVal)
        mid = inorder.index(curVal)

        if len(inorder[:mid +1]) > 0:
            curNode.left = self.helper(preorder[1:mid+1], inorder[:mid])
            
        if len(inorder[mid:]) > 0:
            curNode.right = self.helper(preorder[mid+1:], inorder[mid+1:])
        return curNode

if __name__ == '__main__':
    s = Solution()
    print(s.buildTree([3,9,20,15,7],[9,3,15,20,7]))
    # print(s.buildTree([1,2],[1,2]))
    # print(s.buildTree([3,1,2,4], [1,2,3,4]))