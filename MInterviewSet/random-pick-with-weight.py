# Notes: Using an actual array to represent this is inefficent, i used a dict of range ends instead
# We are relying on order of dictionary keys added which might be bad
# Theres another solution we can leverage a list and bisect

# TC: 
# O(n) for init, we are iterating through the input
# O(n) for pickIndex, we iteraate to find the first key thats bigger then index (we)

class Solution:
    def __init__(self, w: List[int]):
        self.denominator = sum(w)
        self.weightDict = {}

        runningSumForIndex = 0
        for i, e in enumerate(w):
            self.weightDict[runningSumForIndex] = i
            runningSumForIndex += e
        print(self.weightDict)

    def pickIndex(self) -> int:
        randomIndex = random.randrange(0, self.denominator)
        sortedKeys = self.weightDict.keys()
        prevKey = None

        for key in sortedKeys:
            # Find the key thats immediately smaller than the index
            if randomIndex < key:
                break
            prevKey = key

        return self.weightDict[prevKey]

# Way better solution
# TC: 
# O(n) for init, we are iterating through the input
# O(logn) for pickIndex, by using binary search to determine where to input it

import bisect
class Solution:

    def __init__(self, w: List[int]):
        self.weightList = []
        prefixSum = 0
        for i, e in enumerate(w):
            prefixSum += e
            self.weightList.append(prefixSum)

        # Final Sum
        self.denominator = prefixSum

        print(self.weightList)

    def pickIndex(self) -> int:
        randomIndex = random.randint(1, self.denominator)
        leftMostIndex = bisect.bisect_left(self.weightList, randomIndex) # Binary search so log(n)
        print(randomIndex)
        return leftMostIndex

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()