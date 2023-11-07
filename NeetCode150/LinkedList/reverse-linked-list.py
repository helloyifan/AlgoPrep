# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head != None:
            temp = head.next # Hold on to the actual head.next, because we are going to remove it
            head.next = prev # Reverse where it points to 
            prev = head # update prev to be head for next iteration
            head = temp # update head to be the next iteration
            
        return prev

"""
[1,2,3,4,5]
[1,2]
[1]
[]
"""
