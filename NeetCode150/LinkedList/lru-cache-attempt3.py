# Spent 35 mins  failed bvb 
class DoublyLinkedList:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.dict =  {}
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.count = 0

    def deleteHelper(self, key):
        node = self.dict[key]
        nextNode = node.next
        prevNode = node.prev

        # Updating neighbor pointers
        if prevNode != None:
            prevNode.next = nextNode
        if nextNode != None:
            nextNode.prev = prevNode

        # setting head/tail trackers
        if node == self.head:
            self.head =  nextNode
        if node == self.tail:
            self.tail = prevNode

        # not sure if we have to care about is the node we are deleteing is tail or w.e
        return node
    
    def insertToHeadHelper(self, node):
        curHead = self.head
        node.next = curHead
        self.head = node

        # Initalize tail
        if self.tail == None:
            self.tail = self.dict[node.key]
            
        return
    
    def get(self, key: int) -> int:
        ret = -1
        if key in self.dict:
            ret = self.dict[key].val
            node = self.deleteHelper(key)
            self.insertToHeadHelper(node)
        return ret

    def put(self, key: int, value: int) -> None:    
        if not key in self.dict:
            self.dict[key] = DoublyLinkedList(key, value)
            self.insertToHeadHelper(self.dict[key])

            
            # clean up if too many
            if len(self.dict) > self.capacity:
                tailKey = self.tail.key
                self.deleteHelper(tailKey)
                del self.dict[tailKey]

        elif key in self.dict:
            self.dict[key].val = value
            self.deleteHelper(key)
            self.insertToHeadHelper(self.dict[key])
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
