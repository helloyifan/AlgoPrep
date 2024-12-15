# Not:
# Ask if the head node starts at the beginning (it should for this normal variant of this question)
# Pretty trivial if thats the case, just create a dict to map old node to new nodes
# then go through ll again to update random and next
# TC: O(n) for going through it twice
# SC: O(n) for the new nodes stored in node dict

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        nodeDict = {}

        # First pass copy 
        th = head
        while th != None:
            nodeDict[th] = Node(th.val)
            th = th.next

        #print(nodeDict)

        # Seconod pass pointers
        th = head
        while th != None:
            if th.next != None:
                nodeDict[th].next = nodeDict[th.next]

            if th.random != None:
                nodeDict[th].random = nodeDict[th.random]
            th = th.next

        return nodeDict[head]