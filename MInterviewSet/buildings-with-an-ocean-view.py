
from collections import deque

def optimal_oceanView(buildings):
    result = []
    
    runningMax = float('-inf')
    for ib in range(len(buildings)-1, -1, -1): # TC: O(n)
        if buildings[ib] > runningMax:
            result.append(ib)
        runningMax = max(runningMax, buildings[ib])
    return list(reversed(result))

# TC: O(n)
# SC: O(n)
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        #Initiatlize with 0 bcuz rightmost can always see the wayer
        listOfMaxRightSideHeights = deque([0])  #SC: O(n)

        runningMax = float('-inf')
        # second arg 0 bcuz we  want to end at index 1 bcuz we dont care about the  height of the last building
        for ib in range(len(heights)-1, 0, -1): # TC: O(n), 
            runningMax = max(runningMax, heights[ib])
            listOfMaxRightSideHeights.appendleft(runningMax)        
        
        print(listOfMaxRightSideHeights)
        
        result = [] # SC: O(n)
        for i, b in enumerate(heights):
            requiredHeight = listOfMaxRightSideHeights[i] #SC: O(n)
            print(requiredHeight, b)
            if requiredHeight < b:
                result.append(i)   
        
        print(result)
        return result
