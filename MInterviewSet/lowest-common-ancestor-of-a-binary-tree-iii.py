# Note: The Special part of this question is self.parent
# Since we have parent, we just go up until we see a hit
# TC: O(n) since we can be starting at bottom of tree
# SC: O(n) since if we start at bottom, every number is added to the set
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def lowestCommonAncestor(self, p: "Node", q: "Node") -> "Node":
        pPathUp = set()

        copyP = p
        while copyP != None:
            pPathUp.add(copyP.val)
            copyP = copyP.parent

        copyQ = q
        while copyQ != None:
            print(copyQ.val)
            if copyQ.val in pPathUp:
                return copyQ
            copyQ = copyQ.parent

        return None
