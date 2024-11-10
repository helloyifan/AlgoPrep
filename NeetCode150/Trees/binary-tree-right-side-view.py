# Spent 11 mins trying to do it through DFS, but this is a BFS question
# Spent 13 min using list for q (solved in 25mins)

# Time complexity:
# O(n) BFS traversal, we process each node once
# Space complexity:
# O(n) Worst case is that every node ends up in queue q

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        q = [root]
        ret = []
        while len(q) > 0:
            # Last node
            lastNode = q[len(q)-1]

            ret.append(lastNode.val)

            tempQ = []
            #BFS processsing
            while len(q) > 0:
                t = q.pop(0)
                if t.left != None:
                    tempQ.append(t.left)

                if t.right != None:
                    tempQ.append(t.right)
            
            q = tempQ

        return ret