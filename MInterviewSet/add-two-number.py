# Note: LL are backwards
# TC: O(n) where n is the cumulative number of nodes
# SC: O(n) we are creating new nodes everytime

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        retHead = ListNode(0)
        ptr = retHead

        carryOver = False

        # Until both are empty
        while l1 != None or l2 != None: 
            curSum = 0

            # Stop if its empty
            if l1 != None:
                curSum += l1.val
                l1 = l1.next

            # Stop if its empty
            if l2 != None:
                curSum += l2.val
                l2 = l2.next

            if carryOver:
                curSum += 1

            if curSum >= 10:
                carryOver = True
                curSum -=10
            else:
                carryOver = False

            retHead.next = ListNode(curSum)
            retHead = retHead.next

        
        if carryOver:
            retHead.next = ListNode(1)
            retHead = retHead.next #not neede but code consistent

        return ptr.next