from typing import Optional

# Solved on Lc and NC in 30 mins
# Just annoying to think about thats all

# Time Complexity: 
# We reverse nodes linearly: O(n)
# We peek first but thats linear as well O(n)
# Total is O(n) + O(n) so its O(2n) which is still O(n)

# Space Complexity
# O(1) we dont use additional space

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        returnHead = None
        currentTail = None
        while head != None:
            headOfReversedList, oldNextOfHeadReversedList, oldHeadBeforeReversing = self.reverseLinkedList(head, k)

            # After first reversing, 1,2,3 to 3,2,1
            # head of list is 3
            if returnHead == None:
                returnHead = headOfReversedList
            
            # This is 4 after revering 1,2,3
            head = oldNextOfHeadReversedList

            # This is to point 1 -> 6, but we need to reverse 4,5,6 first (we dont do it in first iteration)
            if currentTail != None:
                currentTail.next = headOfReversedList

            currentTail = oldHeadBeforeReversing
        
        return returnHead
    
    def checkEnoughNodes(self, head, k):
        for _ in range(k):
            if head == None:
                return False
            head = head.next
        return True

    def reverseLinkedList(self, head, k):
        if not self.checkEnoughNodes(head, k):
            headOfNotReversedList = head
            oldNextOfHeadReversedList = None # because its the end, we dont need to do it anymore
            return headOfNotReversedList, oldNextOfHeadReversedList, None

        startHead = head
        prev = None
        counter = 0
        while head != None and counter < k:
            counter += 1
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        # For returning
        headOfReversedList = prev
        oldNextOfHeadReversedList = head
        oldHeadBeforeReversing = startHead

        return headOfReversedList, oldNextOfHeadReversedList, oldHeadBeforeReversing
    

test1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))

test2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

sol = Solution()

# Debugging
# sol.reverseLinkedList(test1, 3)
#sol.reverseKGroup(test1, 3)

sol.reverseKGroup(test2, 3)