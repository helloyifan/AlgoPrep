# Tried for another 30 mins, different solution then neetcode
# so its not working correctly,
# insert logic isnt right it doesnt handle existing head Node(0,0 )
# update correctly
class DoublyLinkedList:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {} # key is key value is node
        self.head = DoublyLinkedList(0,0)
        self.tail = DoublyLinkedList(0,0)
        return
    
    def remove(self, node):
        nextNode = node.next
        prevNode = node.prev
        nextNode.prev = prevNode
        prevNode.next = nextNode
        
        return


    def insert(self, node):
        # 2 Adding new
        oldHead = self.head
        oldHead.prev = node
        node.next = oldHead
        self.head = node
        return 

    def get(self, key: int) -> int:
        if not key in self.dict:
            return -1
        
        accessedNode = self.dict[key]
        # move accessed Node to head
        self.remove(accessedNode)
        self.insert(accessedNode)

        return

    def put(self, key: int, value: int) -> None:
        # 1. insert something thats already in 
        if key in self.dict:
            self.remove(self.dict[key])

        newNode = DoublyLinkedList(key, value)
        self.insert(newNode)
        # 2.1 adding new now to dict
        self.dict[key] = newNode

        # 3. if theres too many remove the tail
        if len(self.dict) > self.capacity:
            oldTailPrev = self.tail.prev
            self.remove(self.tail)
            self.tail = oldTailPrev
            del self.dict[oldTailPrev.key]

        return
    

lRUCache = LRUCache(2)
lRUCache.put(1, 10)  # cache: {1: 10}
print(lRUCache.get(1))  # returns 10
lRUCache.put(2, 20)  # cache: {1: 10, 2: 20}
lRUCache.put(3, 30)  # cache: {2: 20, 3: 30}, key 1 was evicted
print(lRUCache.get(2))  # returns 20
print(lRUCache.get(1))  # returns -1 (not found)
# Output looks like 10, 20, -1

# lRUCache = LRUCache(2)
# lRUCache.put(1, 1)  # cache: {1: 1}
# lRUCache.put(2, 2)   # cache: {1: 1, 2: 2}
# print(lRUCache.get(1)) # returns 1
# lRUCache.put(3, 3) # cache: {1: 1, 3: 3}
# print(lRUCache.get(2))   # returns -1
# lRUCache.put(4, 4) # cache: {3:3, 4:4}
# print(lRUCache.get(1))
# print(lRUCache.get(3))
# print(lRUCache.get(4))

# lRUCache = LRUCache(4)
# lRUCache.put(1, 1)
# lRUCache.put(2, 2)
# lRUCache.put(3, 3)
# print(lRUCache.get(1)) # 1
# print(lRUCache.get(2)) # 2
# print(lRUCache.get(4)) # -1
# lRUCache.put(4, 4)
# print(lRUCache.get(1)) # 1
# print(lRUCache.get(2)) # 2
# print(lRUCache.get(3)) # 3
# print(lRUCache.get(4)) # 4
# print(lRUCache.get(2))  # 2
# lRUCache.put(5, 5)
