# Took 50 mins and didnt do it gracefully
# The hint is that, we can reverse the second half of the list
# and then shuffle it in like a deck of cards 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 0 base case.
        if head.next == None:
            return

        # 1. Get number of nodes
        numOfNodes = 0
        temp1 = head
        while temp1 != None:
            temp1 = temp1.next
            numOfNodes += 1
        
        # 2. Get to the halfway node
        halfwayIndex = numOfNodes//2
        temp2 = head
        temp2Counter = 0
        temp2Prev = None
        while temp2Counter < halfwayIndex:
            temp2Prev = temp2
            temp2 = temp2.next
            temp2Counter += 1


        # 3. reverse the second half of the linkedlist
        newHead = self.reverseLinkedList(temp2)
        # 3.5 seperate the twolists (so there isnt a cycle)
        temp2Prev.next = None

        # 4. shuffle it in
        retLL = self.shuffleInTwoLL(head, newHead)

    def reverseLinkedList(self, head):
        temp = None
        prev = None
        while head != None:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev # the new head
    
    def shuffleInTwoLL(self, head1, head2):
        # print("---")
        # self.printLinkedList(head1)
        # print("=--=-")
        # self.printLinkedList(head2)

        starting = ListNode(0) # dummy
        newHead = starting

        while head1 != None and head2 != None:
            newHead.next = head1
            head1 = head1.next
            newHead = newHead.next

            newHead.next = head2
            head2 = head2.next
            newHead = newHead.next
        
        
        if head1 == None and head2 != None:
            newHead.next = head2
        elif head1 != None and head2 == None:
            newHead.next = head1
        # print("=fin--=-")
        # self.printLinkedList(starting)
        return starting

    def printLinkedList(self, head):
        while head != None:
            print(head.val)
            head = head.next
        
        #print("fin node next")