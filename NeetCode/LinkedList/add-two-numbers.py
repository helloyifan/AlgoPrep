# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        retHead = ListNode()
        ptr = retHead
        carryOver = False

        while ((not l1 is None) or (not l2 is None)):
            sumVal = 0 

            if (not l1 is None):
                sumVal += l1.val
                l1 = l1.next

            if (not l2 is None):
                sumVal += l2.val
                l2 = l2.next


            if (carryOver):
                sumVal += 1
                carryOver = False

            if (sumVal >= 10):
                sumVal -= 10
                carryOver = True
                
            print(sumVal)
            ptr.next = ListNode(sumVal)
            ptr = ptr.next

        
        # If theres that pesky remainder 1
        if (carryOver):
            ptr.next = ListNode(1)
            # Not needed but these lines make me happy ;)
            carryOver = False 
            ptr = ptr.next

        return retHead.next

'''
[9,9,9,9,9,9,9]
[9,9,9,9]
[2,4,3]
[5,6,4]
[1,2]
[1,2,3,4,5,6,7,8,9]
'''