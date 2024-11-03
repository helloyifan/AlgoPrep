# ATtempt 1: 40mins
# Passed NC but doesnt pass LC
# Time Complexity:
# Set: O(c)
# Get: O(nlogn + logn)
    # n for converying from dict to list
    # nlogn for sorting
    # logN for binary search
# Space Complexity:
# O(n), each record is stored in our data structures

from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.hash = defaultdict(dict) #{key: {time: val}}
        return
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash[key][timestamp] = value
        return
    def get(self, key: str, timestamp: int) -> str:
        if not key in self.hash or len(self.hash[key]) == 0:
            return ''

        entry = self.hash[key]        
        if timestamp in entry:
            return entry[timestamp]
        
        # Binary Search
        binSearchList = [(k,v) for k,v in entry.items()]
        binSearchList.sort(key=lambda x: x[0])

        start, end = 0, len(binSearchList) -1
        prevValThatsSmaller = None
        while start <= end:
            mid = (start + end)//2
            if binSearchList[mid][0] < timestamp:
                prevValThatsSmaller = binSearchList[mid]
                start = mid+1
            elif binSearchList[mid][0] > timestamp:
                end = mid-1
            else:
                print("something bad happened")

        #print("prevValThatsSmaller: ", prevValThatsSmaller)
        if prevValThatsSmaller == None:
            return ""
        return prevValThatsSmaller[1]

# timeMap = TimeMap()
# timeMap.set("alice", "happy", 1)
# print(timeMap.get("alice", 1))    # Output: "happy"
# print(timeMap.get("alice", 2))    # Output: "happy"
# timeMap.set("alice", "sad", 3)
# print(timeMap.get("alice", 3))    # Output: "sad"

# Initialize TimeMap instance
timeMap = TimeMap()

# Perform operations
timeMap.set("test", "one", 10)
timeMap.set("test", "two", 20)
timeMap.set("test", "three", 30)

# Retrieve values
print(timeMap.get("test", 15))   # Expected output: "one" (closest timestamp <= 15 is 10)
print(timeMap.get("test", 25))   # Expected output: "two" (closest timestamp <= 25 is 20)
print(timeMap.get("test", 35))   # Expected output: "three" (closest timestamp <= 35 is 30)