from typing import List

# Notes:
# Step 1. Create a debt list of numbers not dict
# Step 2. Backtrack with the intent to find min transactions
# Recursion will be managed by incremetning starting index def backtracking(curIndex=0, debtList):
# We know that we are getting closer when curIndex * curAttempResolvingDebt is a neg number
# Backtrack modify and backtrack cleanup

# TC: O((T-1)!) as there exists t-1 persons 
# SC: O(T)

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        debt = {} # O(T)
        # Step 1 preprocess, by converting to debt datastructure
        for t in transactions: # O(T)
            fromPerson, toPerson, amount = t[0], t[1], t[2]

            if not fromPerson in debt:
                debt[fromPerson] = 0
            debt[fromPerson] -= t[2]

            if not toPerson in debt:
                debt[toPerson] = 0
            debt[toPerson] += t[2]

        # For our algo we need debt in list format
        debtList = [] # O(T)
        for key in debt: # O(T)
            debtList.append(debt[key])
        print(debtList)

        # Step 2. Specific algorithm to settle debtWith backtracking
        def backtracking(curIndex, debtList):
            if curIndex == len(debtList):
                return 0

            if debtList[curIndex] == 0: # If altready debt free move forwards
                return backtracking(curIndex+1, debtList)
           
            curDebt = debtList[curIndex] # current value we are workth with

            minVal = float('inf')
            for i in range(curIndex+1, len(debtList)): # We iterate one less time everytime so #O(T!)
                curAttempResolvingDebt = debtList[i]

                if curDebt * curAttempResolvingDebt < 0: # Neg number means we are closer to resolving debt
                    debtList[i] += curDebt
                    minVal = min(minVal, 1+ backtracking(curIndex+1, debtList))
                    debtList[i] -= curDebt #backtrack cleanup

                    # I think this is optional
                    if curDebt + curAttempResolvingDebt == 0:
                        break
            return minVal
        
        minVal = backtracking(0, debtList)
        return minVal
    
sol = Solution()
#print(sol.minTransfers([[0,1,10],[2,0,5]]))
print(sol.minTransfers( [[0,1,10],[1,0,1],[1,2,5],[2,0,5]]))