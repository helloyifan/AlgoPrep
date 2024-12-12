

from typing import List
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # TC: O(N * logk) 
    # where N is the total number of nodes across all lists,
    # k is the number of lists, (we  always half the nu,ber of lists)
    # SC: O(1)

    # Example of why divide and conquer is faster
    # 1:4, 2:4, 3:4, 4:4
    # [1,2] took 8 comparsions, 
    # [3,4] took 8 compariions
    # [1,2,3,4] took 16 comparions 
    # in total 32 comparions

    # Sequentially
    # 1:4, 2:4, 3:4, 4:4
    # [1,2] took 8 comparsions, 
    # [1,2,3] took 12 compariosn
    # [1,2,3,4] took 16 compartions
    # in total took 36 comparions
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Go 2 at a atime
        while len(lists) > 1:
            print(lists)
            tempLists = []
            for i in range(0, len(lists), 2):
                ret = self.merge2Lists(lists[i], lists[i+1] if len(lists) > i+1 else None)
                tempLists.append(ret)
            
            lists = tempLists

        return lists[0]
    
    def merge2Lists(self, list1, list2):
        if list2 == None:
            return list1

        start = ListNode(0)
        ptr = start 
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                start.next = list1
                list1 = list1.next
            else:
                start.next = list2
                list2 = list2.next
            start = start.next
        
        if list1 == None and list2 != None:
            start.next = list2
        elif list1 != None and list2 == None:
            start.next = list1
        
        return ptr.next

    # TC: O(k * N) where k is the is length of the list and N is the TOTAL SIZE
    # because in the worst case we always pick the last one every iteration
    # SC: O(1)
    def OkN_mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ret = ListNode(0)
        startingTracker = ret

        while True:
            minV = float('inf')
            minIndex = None
            didSomething = False
            for i, e in enumerate(lists):
                if e != None and e.val < minV:
                    minV = e.val
                    minIndex = i
                    didSomething = True
            
            if didSomething == False:
                break
            
            ret.next = lists[minIndex]
            ret = ret.next
            lists[minIndex] = lists[minIndex].next

        return startingTracker.next
    
    # This is still technically O(k*n) merges 
    # Because for 4 lists, the first list we are comapring (list1+list2+list3), list4
    # But somehow this is faster than the second solution, not as fast as the first
    # TC: O(k*n)
    def Sequentially_MergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ret  = lists[0]
        
        # Go 2 at a atime
        for i in range(1, len(lists)):
            curList = lists[i]
            ret = self.merge2Lists(ret, curList)

        return ret




sol = Solution()
list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))

# print(sol.merge2Lists(list1, list2))
sol.mergeKLists([list1, list2, list3])