
from typing import Optional
# spent 30 min on the wrong way
#   - tried to map the random back to val and val back to random (it was conveluted)
# Spent another 30 min on the second attempt which makes more logical sense
#   - basically maped the old node to the new node by reference (not val bcuz of duplicate value)
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def attempt1(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        createdHead = None
        createdPtr = None
        headPtr1 = head

        mapOfRandomVal = {}
        mapOfRandomPtr = {}

        while headPtr1:
            if headPtr1.random:
                mapOfRandomVal[headPtr1.random.val] = headPtr1.val

            if createdHead == None:
                createdHead = Node(headPtr1.val)
                createdPtr = createdHead
            else:
                createdPtr.next = Node(headPtr1.val)
                createdPtr = createdPtr.next
            
            headPtr1 = headPtr1.next


        headPtr2 = createdHead
        while headPtr2:
            if headPtr2.val in mapOfRandomVal:
                reversedPtr = mapOfRandomVal[headPtr2.val]
                mapOfRandomPtr[reversedPtr] = headPtr2

            headPtr2 = headPtr2.next

        headPtr3 = createdHead
        while headPtr3:
            if headPtr3.val in mapOfRandomPtr:
                headPtr3.random = mapOfRandomPtr[headPtr3.val]
    
            headPtr3 = headPtr3.next
        return createdHead
    
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        headPtr1 = head
        createdHead = None
        createdHeadPtr = None

        existingToCreatedMap = {}

        while headPtr1:
            if createdHead == None:
                createdHead = Node(headPtr1.val)
                createdHeadPtr = createdHead
            else:
                createdHeadPtr.next = Node(headPtr1.val)
                createdHeadPtr = createdHeadPtr.next
            
            existingToCreatedMap[headPtr1] = createdHeadPtr
            headPtr1 = headPtr1.next

        headPtr2 = head
        createdHeadPtr2 = createdHead
        print(f"{existingToCreatedMap}")
        while headPtr2: 
            print("headPtr2.val: ", headPtr2.val)
            
            if headPtr2.random != None and headPtr2.random in existingToCreatedMap:
                print("headPtr2.random.val: ", headPtr2.random.val)
                createdHeadPtr2.random = existingToCreatedMap[headPtr2.random]

            headPtr2 = headPtr2.next
            createdHeadPtr2 = createdHeadPtr2.next


        return createdHead