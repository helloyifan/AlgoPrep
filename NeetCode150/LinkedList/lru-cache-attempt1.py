# 40 min, spent trying to debug this stupid linked list thing
# Theres still something wrong wiht it but i dont see a point of trying this anymore

class LinkedListNode:
    val = None
    next = None
    def __init__(self, val):
        self.val = val

class LRUCache:
    d = None
    lastUsedNodeLL = None
    counter = 0 
    capacity = None

    def __init__(self, capacity: int):
        self.d =  {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.d:
            self.setNewHeadHelper(key)
            return self.d[key] 
        else :
            return -1

    def put(self, key: int, value: int) -> None:
        self.d[key] = value
        self.setNewHeadHelper(key)
        return

    def cleanUpHelper(self):

        head = self.lastUsedNodeLL
        prevNode = None
        while head.next != None:
            prevNode = head
            head = head.next
        # Delete from dict
        if head.val != self.lastUsedNodeLL.val:
            if head.val in self.d:
                del self.d[head.val]
        # Delete from cache
        if prevNode != None:
            prevNode.next = None
        self.counter -= 1

    def setNewHeadHelper(self, key):
        newNode = LinkedListNode(key)
        newNode.next = self.lastUsedNodeLL
        self.lastUsedNodeLL = newNode
        self.counter += 1

        if self.counter > self.capacity:
            self.cleanUpHelper()

        return

# lRUCache = LRUCache(2)
# lRUCache.put(1, 10)  # cache: {1: 10}
# print(lRUCache.get(1))  # returns 10
# lRUCache.put(2, 20)  # cache: {1: 10, 2: 20}
# lRUCache.put(3, 30)  # cache: {2: 20, 3: 30}, key 1 was evicted
# print(lRUCache.get(2))  # returns 20
# print(lRUCache.get(1))  # returns -1 (not found)

lRUCache = LRUCache(2)
lRUCache.put(1, 1)  # cache: {1: 1}
lRUCache.put(2, 2)   # cache: {1: 1, 2: 2}
print(lRUCache.get(1)) # returns 1
lRUCache.put(3, 3) # cache: {1: 1, 3: 3}
print(lRUCache.get(2))   # returns -1
lRUCache.put(4, 4) # cache: {3:3, 4:4}
print(lRUCache.get(1))
print(lRUCache.get(3))
print(lRUCache.get(4))

