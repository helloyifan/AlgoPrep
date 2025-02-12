# Problem is that im not finding the best possible thing to remove
# I can start hold the right most and go left to right, for the left value
# But that doesnt mean its the optimal action to take

# Irl answer is with back tracking
from typing import List
from collections import defaultdict

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        debt = defaultdict(int)
        for t in transactions:
            fromId, toId, value = t[0], t[1], t[2]
            debt[toId] -= value
            debt[fromId] += value # Do we keep track of fromId and toId

        debtList = []
        for key in debt:
            debtList.append(debt[key])
        
        debtList.sort() # Does reverseing the list make it so we can optimal?
        
        print(debt)
        print(debtList)

        transactionCounter = 0 
        while len(debtList) > 0:
            print(debtList)
            curVal = debtList.pop()

            minDiffSoFar = float('inf')
            idxToRemove = None
            # Find the the smallest value you can pop
            for j in range(len(debtList)):
                nextVal = debtList[j]
                if curVal * nextVal < 0: # Negative number means we are getting closer
                    if abs(curVal + nextVal) < minDiffSoFar:
                        minDiffSoFar = abs(curVal + nextVal)
                        idxToRemove = j
                    
            if idxToRemove != None:
                nextVal = debtList.pop(idxToRemove) #doing this so outside of loop  context
                transactionCounter += 1
                newVal = curVal + nextVal
                if newVal != 0:
                    debtList.append(newVal)

        print(transactionCounter)
        return transactionCounter
    

sol = Solution()

# sol.minTransfers([[0,1,10],[2,0,5]]) # 2
# sol.minTransfers( [[0,1,10],[1,0,1],[1,2,5],[2,0,5]]) # 1
# sol.minTransfers( [[0,1,1],[1,2,1],[2,0,1]]) # 0
sol.minTransfers([[0,2,4],[1,2,4],[3,4,5]]) # 3

# 1: 10, 0: 5