# Note: Build ret list from 2 input list
# TC: O(n) where n is the total number of node (first and second list)
# SC: O(k) where k is the number of intersections, which grows at the same rate as O(n)
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        firstListIndex = 0
        secondListIndex = 0
        
        retIntervalIntersection = []
        while firstListIndex < len(firstList) and secondListIndex < len(secondList):
            firstV = firstList[firstListIndex]
            secondV = secondList[secondListIndex]

            intersectionStart = max(firstV[0], secondV[0])
            intersectionEnd = min(firstV[1], secondV[1])

            # if End is b4 Start then not a valid result
            if intersectionStart <= intersectionEnd:
                retIntervalIntersection.append([intersectionStart, intersectionEnd])

            # Only step up the one with smaller end value
            if firstV[1] > secondV[1]:
                secondListIndex += 1
            else:
                firstListIndex += 1

        print(retIntervalIntersection)
        return retIntervalIntersection