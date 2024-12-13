# Notes:
# Define Doubly linked list
# Set default self.head and self.tail, NEVER UPDATE THEM DIRECTLY
# point self.head.next to tail and inverse

# TC: 
# GET: O(1) lookup with dict, add/remove are linear
# PUT: O(1) add/remove are linear

# SC: 
# O(n) where n is capacity - we are maintain a dict as well as DLL based on the number of nodes we are inserting

class DDL:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity =capacity
        self.dict = {}
        self.head = DDL(0,0) # Tip initalize head and tail for less pain
        self.tail = DDL(0,0) # NEVER UPDATE HEAD AND TAIL DIRECTLY
        self.head.next =self.tail # With this relationship existing, we don't need to manage it in our code
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            self.removeNodeFromCache(node.key)
            self.addNodeToCache(node.key, node.value)

            print('get: ', node.value)
            return node.value
        print('get: ', -1)
        return -1
        

    def put(self, key: int, value: int) -> None:
        # If it already exists
        if key in self.dict:
            self.removeNodeFromCache(key)
        
        self.addNodeToCache(key, value)
        
        # Do we need to remove old one?
        if len(self.dict) > self.capacity:
            self.removeNodeFromCache(self.tail.prev.key)


    def addNodeToCache(self, key, value):
        node = DDL(key, value)

        oldNonZeroHead = self.head.next
        self.head.next = node
        node.prev = self.head # O is before what we inserted

        node.next = oldNonZeroHead #oldNonZeroHead points to new node back and forth
        oldNonZeroHead.prev = node
        self.dict[key] = node

    def removeNodeFromCache(self, key):
        print(key)
        node = self.dict[key]

        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode

        del self.dict[key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)