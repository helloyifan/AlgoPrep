# Solved in 20mins from intuiton
# Time:
# Factors n for number of cards, k for number of types of cards
# Counting cards: O(n)
# Sorting cards: O(klogk)
# Organizing cards: O(k*groupSize) because in the worst case each key we have the whole list of cards
# Time final: O(n + klogk + k*groupsize)

# Space: 
# counter: O(k) for the card types
# curHand: O(groupSize)
# Space Final: O(k + groupSize)


from typing import List
from collections import defaultdict

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counter = defaultdict(int)

        for card in hand:
            counter[card] +=1


        sortedKeys = list(counter.keys())
        sortedKeys.sort()
        
        for startingKey in sortedKeys: # But what if you have the same hand
            if not startingKey in counter or counter[startingKey] == 0:
                continue

            curHand = defaultdict(int)
            minAmountOfCard = float('inf')
            # what if therse 2 of the same hand
            # we cant just do one at a time
            fastFailed = False
            for i in range(startingKey,startingKey+groupSize):
                if not i in counter:
                    fastFailed = True
                    break

                curHand[i] += counter[i]
                minAmountOfCard = min(minAmountOfCard, counter[i])


            if fastFailed == True:
                break

            for i in list(curHand.keys()):
                counter[i] -= minAmountOfCard
        
        finRet = True
        for i in counter:
            if counter[i] != 0:
                finRet = False
                break

        print(counter)
        print(finRet)
        
        return finRet

sol = Solution()
sol.isNStraightHand([1,2,4,2,3,5,3,4], 4) # True
sol.isNStraightHand([1,2,3,3,4,5,6,7], 4) # False
sol.isNStraightHand([1,2,3,4,5], 4) # false