# Took 10mins,
# With heaps and priority queue this question isnt a hard, but i wonder if thats not the point of the question.

import heapq

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        h = []
        for l in lists:
            while l:
                heapq.heappush(h, (l.val, l))
                l = l.next

        # Edge case where input is [[]] or []
        if len(h) == 0:
            return None

        returnHead = heapq.heappop(h)[1]
        head = returnHead
        while h:
            popped = heapq.heappop(h)[1]
            head.next = popped
            head = head.next

        # Make sure the end doesnt point to anything
        head.next = None

        return returnHead