# Good old tutorise nad hare question
# Took 2 minutes, but im not sure if this code is the most elegant, i wouldnt study this 

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Base case
        if head == None:
            return False
        elif head.next == None:
            return False

        h, t = head.next, head

        while h != None:
            if h == t: #We are not doing h.val and t.val bcuz question allows same val
                return True

            # This is just checks to make sure we wont hit out of bound
            if h.next == None or h.next.next == None:
                return False

            h = h.next.next
            t = t.next
        
        return False