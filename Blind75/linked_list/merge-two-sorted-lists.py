# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        ret = ListNode(val=float('-inf'))
        startingPoint = ret
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                ret.next = list1
                list1 = list1.next
            else:
                ret.next = list2
                list2 = list2.next
            ret = ret.next

        if list1 != None:
            ret.next = list1
        
        if list2 != None:
            ret.next = list2

        return startingPoint.next
if __name__ == "__main__":
    s = Solution()
