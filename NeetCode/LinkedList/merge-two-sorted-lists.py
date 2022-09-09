# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        start = ListNode() #Basic the genius is instead of managing the base case, just have a starting prt thats not in answer (start.next is start of answer)
        cur = start 
        
        while (list1 and list2):
            if (list1.val < list2.val):
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
            
        if (list1 != None):
            cur.next = list1
        elif(list2 != None):
            cur.next = list2
        
        return start.next

'''
[1,3,4]
[1,2,4]
[]
[] 
[]
[0]
[1,1,1,1]
[1,1,1]
'''