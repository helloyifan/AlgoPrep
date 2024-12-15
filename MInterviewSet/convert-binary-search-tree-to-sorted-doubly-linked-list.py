# Note: understand inorder traversal left -> process -> right
# Figure out how to hold value of first and last outside of DFS recursions
# figure out how to hold prev in outside of DFS recursion
# Firts points to last and last back to first

# TC: O(n) for DFS
# SC: O(n) for DFS call stack usage

from typing import Optional
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return None

        prevNode = [None]
        first = [None]
        last = [None]

        def dfs(root):
            if root == None:
                return
        
            l = dfs(root.left)

            if first[0] == None:
                first[0] = root

            # in order processing

            if prevNode[0] != None:
                root.left = prevNode[0]
                prevNode[0].right = root

            prevNode[0] = root

            last[0] = root # just keep overwriting last, the last time we overwrite will be correct
            r = dfs(root.right)
            

            return root

        dfs(root)
        print(prevNode[0].val)
        print(first[0].val)
        print(last[0].val)
        
        # make it circular
        first[0].left = last[0]
        last[0].right = first[0]

        return first[0]
# [2,1,3]
