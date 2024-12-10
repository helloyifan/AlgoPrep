# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        node1 = list1
        node2 = list2
        dummyNode = ListNode()
        newNode = dummyNode

        while node1 != None and node2 != None:
            if node1.val > node2.val:
                newNode.next = node2
                node2 = node2.next
            else:
                newNode.next = node1
                node1 = node1.next
            newNode = newNode.next
        
        if node1 != None:
            newNode.next = node1
        elif node2 != None:
            newNode.next = node2

        return dummyNode.next