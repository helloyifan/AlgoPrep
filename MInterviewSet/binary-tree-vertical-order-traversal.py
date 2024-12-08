
# Notes: Use a deque.popleft() (O(1) instead of .pop(0) (O(n))
# TC: BFS is O(n), processing output is  O(nlogn) because of sorting so total is O(nlogn), but technically i can think of 
# using bisect instead of sorting
# SC: dd is O(n), dq is O(n) so total is O(n)

from typing import List
from collections import defaultdict
from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        dd = defaultdict(list)
        dq = deque([(0, root)]) # Root at col number 0

        while len(dq) > 0:
            tempDq = deque([])
            while len(dq) > 0:
                e = dq.popleft() # insetad of .pop(0)
                index = e[0]
                node = e[1]

                dd[index].append(node.val)
                if node.left != None:
                    tempDq.append((index-1, node.left))
                if node.right != None:
                    tempDq.append((index+1, node.right))
            dq = tempDq

        # post process dd:
        sortedKeys = sorted(dd.keys())
        ret = []
        for i in sortedKeys:
            ret.append(dd[i])
        print(ret)
        return ret