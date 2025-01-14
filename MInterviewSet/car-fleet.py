# notes: THey dont tell you, but a car cound finish at a non-int time, it could finish at time 0.5
# meaning we hanve to handle timeToComplete from division
# TC: O(nlogn): Because we use O(n) time for preprocess and O(n) for main processing, and we use O(nlogn) for sorting
# SC: O(n): O(n) for fleets for number of position and speed
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []

        for i in range(len(position)): # O(n)
            fleets.append([position[i], speed[i]])
        
        fleets.sort(key=lambda x: -x[0]) #O(nlogn)

        timeToComplete = []

        slowestTimeToComplete = float('-inf')
        numOfFleets = 0
        for fleet in fleets: # O(n)
            remainingDistance =  target - fleet[0]
            timeToComplete = remainingDistance / fleet[1]
            print(timeToComplete)
            if timeToComplete > slowestTimeToComplete:
                slowestTimeToComplete = timeToComplete
                numOfFleets += 1


        return numOfFleets