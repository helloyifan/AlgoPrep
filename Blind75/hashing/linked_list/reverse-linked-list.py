# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp = None
        prevNode = None
        while head != None:
            tmp = head.next
            head.next = prevNode
            prevNode = head
            head = tmp
        return prevNode