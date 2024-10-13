# I solved it in 30 min and it passes on both neetcode and leetcode
# But i think i didnt do it to the intent of the question of using a LL or a DLL, i used a list and list.remove(key)
# remove(n) is O(n) runtime

# Time Complexity: 
# Put is O(n) where n is capacity (since this is required to be O(1), this solution is incorrect)
# Get is O(1)
class LRUCache:
    def __init__(self, capacity: int):
        self.dict =  {}
        self.cache = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        ret = -1
        if key in self.dict:
            ret = self.dict[key]
            self.updateCache(key)
        return ret

    def put(self, key: int, value: int) -> None:
        self.updateCache(key)
        self.dict[key] = value
        return
    
    def updateCache(self, key):
        if key in self.cache:
            self.cache.remove(key)
        self.cache.insert(0, key)
        if len(self.cache) > self.capacity:
            deletedNode = self.cache.pop()

            # if we are getting something, thats also the next to be deleted, dont delete
            if deletedNode in self.dict: 
                # only delete if we are sure we dont need it
                del self.dict[deletedNode]


# lRUCache = LRUCache(2)
# lRUCache.put(1, 10)  # cache: {1: 10}
# print(lRUCache.get(1))  # returns 10
# lRUCache.put(2, 20)  # cache: {1: 10, 2: 20}
# lRUCache.put(3, 30)  # cache: {2: 20, 3: 30}, key 1 was evicted
# print(lRUCache.get(2))  # returns 20
# print(lRUCache.get(1))  # returns -1 (not found)

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

lRUCache = LRUCache(4)
lRUCache.put(1, 1)
lRUCache.put(2, 2)
lRUCache.put(3, 3)
print(lRUCache.get(1)) # 1
print(lRUCache.get(2)) # 2
print(lRUCache.get(4)) # -1
lRUCache.put(4, 4)
print(lRUCache.get(1)) # 1
print(lRUCache.get(2)) # 2
print(lRUCache.get(3)) # 3
print(lRUCache.get(4)) # 4
print(lRUCache.get(2))
lRUCache.put(5, 5)

