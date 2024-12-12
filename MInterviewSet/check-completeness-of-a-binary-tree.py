# TC: O(n) In worst case we visit everynode once
# SC: O(n) The maximum number of nodes at a level is the width of the tree, which is proportional to O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])

        while len(q) > 0:
            tempQ = deque([])
            sawNone = False
            while len(q) > 0:
                cur = q.pop()
                if cur == None:
                    sawNone = True
                else:
                    if sawNone == True:
                        return False

                    tempQ.appendleft(cur.left) # can be none when apeending
                    tempQ.appendleft(cur.right) 
            

            # If we see a None, we dont do BFS anymore

            # ensure tempQ is empty
            if sawNone == True:
                for item in tempQ:
                    if item != None:
                        return False
            q = tempQ
                
        return True