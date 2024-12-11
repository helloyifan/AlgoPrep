# TC: O(n)
# SC: O(logN) if its a balanced tree, O(n) otherwise

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root, level, ret):
            if root == None:
                return
            
            if len(ret) == level:
                ret.append(root.val)
            
            dfs(root.right, level+1, ret) # WE JUST GO RIGHT FIRST
            dfs(root.left, level+1, ret) # INSTEAD OF LEFT FIRST
            return
        ret = []
        dfs(root, 0, ret)
        
        return ret

# DFS usecase, 
# TC: O(n) because we have to add every node to queue
# SC: O(n) because the max stack size will grove with size of input

# However since BFS, at most only half of the input will need to bei n memory 
# so its O(n/2) rounded up to O(n)

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []

        q = deque([root])
        ret = []
        while len(q) >0:
            tempQ = deque([])
            # Last element is rightmost
            rightMostElement = q[len(q)-1]
            ret.append(rightMostElement.val)

            while len(q)>0:
                cur = q.popleft()
                if cur.left != None:
                    tempQ.append(cur.left)
                if cur.right != None:
                    tempQ.append(cur.right)
            q = tempQ
        return ret