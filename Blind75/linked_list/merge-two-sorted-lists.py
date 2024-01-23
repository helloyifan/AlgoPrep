# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution():
    def mergeList(self, node1, node2):
        ret = None
        while node1 != None and node2 != None:
            if node1.val > node2.val:
                if ret == None:
                    ret = node1
                else:
                    ret.next = node1
                    ret = ret.next
                node1 = node1.next
            else:
                if ret == None:
                   ret = node2
                   ret = ret.next
                node2 = node2.next

        return ret

if __name__ == "__main__":
    # Creating nodes
    node1 = ListNode(1)
    node2 = ListNode(2)
    node4 = ListNode(4)
    # Linking nodes
    node1.next = node2
    node2.next = node4

    nodeb1 = ListNode(1)
    nodeb3 = ListNode(3)
    nodeb4 = ListNode(4)
    # Linking nodes
    nodeb1.next = nodeb3
    nodeb3.next = nodeb4

    s = Solution()
    print(s.mergeList(node1, nodeb1))