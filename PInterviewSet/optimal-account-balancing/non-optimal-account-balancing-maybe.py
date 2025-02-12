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
            curVal = debtList.pop()

            valToRemove = None

            # Find the the smallest value you can pop
            for j in range(len(debtList)):
                nextVal = debtList[j]

                if curVal * nextVal < 0: # Negative number means we are getting closer
                    valToRemove = nextVal
                    break

            if valToRemove != None:
                nextVal = debtList.pop(j) #doing this so outside of loop  context
                transactionCounter += 1
                newVal = curVal + nextVal
                if newVal != 0:
                    debtList.append(newVal)

        print(transactionCounter)
        return transactionCounter