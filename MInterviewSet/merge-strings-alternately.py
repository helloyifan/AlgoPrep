# Note: Avoid string concatenation as its O(n) run time and using it in a loop is O(n^2)
# its must better to append list(O(1)) and ''.join O(n) at the end for O(n)

# TC: O(n) because the while loop grows at the same rate the shorter word is growing
# SC: O(n) for the new string we are building 
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        indexForBothList = 0

        newString = []

        while indexForBothList < len(word1) and indexForBothList < len(word2): #O(n)
            #newString = newString + word1[indexForBothList] + word2[indexForBothList] #String  (note string concatenation is O(n) itself)
            newString.append(word1[indexForBothList])
            newString.append(word2[indexForBothList])

            indexForBothList +=1
        
        if indexForBothList < len(word1):
            #newString = newString + word1[indexForBothList:]
            newString.append(word1[indexForBothList:])

        if indexForBothList < len(word2):
            #newString = newString + word2[indexForBothList:]
            newString.append(word2[indexForBothList:])

        return ''.join(newString)