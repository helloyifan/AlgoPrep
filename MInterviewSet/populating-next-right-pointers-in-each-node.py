'''
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


###        1
###      2 -> 3 
### 4 -> 5 ->6 -> 7 -> None

# TC: O(n) for processing BST in BFS
# SC: O(2^(heightOfTheTree)) and height of the tree is O(logn) = O(2^(logn)) = O(n)
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return None
        
        ## BFS
        q = deque([root])
        
        while len(q) >0:
            tempQ = deque([])
            while len(q) > 0:
                cur = q.popleft()
                
                if len(q) > 0:
                    nextNode = q[0]
                    cur.next = nextNode
                
                if cur.left != None:
                    tempQ.append(cur.left)
                if cur.right != None:
                    tempQ.append(cur.right)
            
            q = tempQ
        
        return root
    
