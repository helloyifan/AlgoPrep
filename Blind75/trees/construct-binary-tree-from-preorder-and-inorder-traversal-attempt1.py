# SPent 50 mins, not totally collrect but close

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
        if len(preorder) <= 0 or len(inorder) <= 0:
            return None

        curVal = preorder[0]
        print(curVal)
        curNode = TreeNode(curVal)
                
        l = self.helper(preorder[1:], inorder[:inorder.index(curVal)])
        r = self.helper(preorder[2:], inorder[inorder.index(curVal)+1:])
        curNode.left = l
        curNode.right = r
        
        return curNode
    

if __name__ == '__main__':
    s = Solution()
    print(s.buildTree([3,9,20,15,7],[9,3,15,20,7]))