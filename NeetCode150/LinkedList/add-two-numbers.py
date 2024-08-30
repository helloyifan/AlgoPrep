# Tried for 20mins and failed bcuz i suck n
# Tried again and got it in 5mins

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        head = dummy

        carryOver = 0
        while l1 != None or l2 != None:
            curSum = 0
            if carryOver > 0:
                curSum += 1
                carryOver = 0

            if l1 != None:
                curSum += l1.val
                l1 = l1.next
            
            if l2 != None:
                curSum += l2.val
                l2 = l2.next
            
            if curSum >= 10:
                curSum -= 10
                carryOver += 1

            head.next = ListNode(curSum)
            head = head.next

        if carryOver > 0:
            head.next = ListNode(1)
            caryOver = 0 

        return dummy.next