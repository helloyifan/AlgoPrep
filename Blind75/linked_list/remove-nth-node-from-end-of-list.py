# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        # Find length
        headFinder = head
        linkedListLength = 0
        while headFinder != None:
            linkedListLength += 1
            headFinder = headFinder.next
        
        # Calculate nth node from the end
        # (or rather num of moves to get there)
        nthNodePos = linkedListLength - n
        
        # Edge case where we want to remove first node
        if nthNodePos == 0:
            return head.next

        # Travel to nthNode
        prev = None
        hTemp = head
        for i in range(0, nthNodePos):
            prev = hTemp
            hTemp = hTemp.next

        # Remove
        prev.next = hTemp.next

        return head