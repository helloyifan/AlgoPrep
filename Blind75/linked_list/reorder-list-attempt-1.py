# Attempt took 30mins

# technically my solution has time complexity of (O n^2) (or maybe thats debatable)
# TLDR works but its too slow 

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        h, t = head, head
        prevHead = None

        while t != None:
            # At the end this is to know we are done
            if prevHead != None and t.next == prevHead: # We check t.next to make sure its not a linked backand fourth
                t.next = None
                return head

            h = t
            # Find the last in the list
            while h.next != None and h.next != prevHead:
                h = h.next
            
            # Do the swaps
            # set temp (will be lost)
            temp = t.next
            # tail points to head
            t.next = h
            # move tail up
            t = temp
            h.next = t
            prevHead = h

        return head