from typing import List


# Notes:
# For Printing path, we need to keep track of key to index in our list
# At the end of our traversal, we have our path
# We keep our path before we backtrack
# The best path will have the lowest numbers of transactions

import copy
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
        indexToNameMap = {} # NEW For printing path
        indexCount = 0
        for key in debt: # O(T)
            debtList.append(debt[key])
            indexToNameMap[key] = indexCount # NEW For printing path
            indexCount += 1
        print('debtList: ', debtList)

        # Step 2. Specific algorithm to settle debt
        # With backtracking?
        
        best_path = []
        def backtracking(curIndex, debtList, path):
            nonlocal best_path # This is to ignored best_path and use the one at the above scope
            if curIndex == len(debtList):
                # At the end of our traversal, we have our path
                # We keep our path before we backtrack
                # The best path will have the lowest numbers of transactions
                if not best_path or len(path) < len(best_path): 
                    best_path = path[:]
                return 0

            if debtList[curIndex] == 0:
                 # do something else
                return backtracking(curIndex+1, debtList, path)

            minVal = float('inf')
            for i in range(curIndex+1, len(debtList)): # We iterate one less time everytime so #O(T!)
                curDebt = debtList[curIndex]
                curAttempResolvingDebt = debtList[i]

                if curDebt * curAttempResolvingDebt < 0: # Neg number means we are closer to resolving debt
                    debtList[i] += curDebt
                    path.append((indexToNameMap[curIndex], indexToNameMap[i], curDebt))

                    minVal = min(minVal, 1 + backtracking(curIndex + 1, debtList, path))

                    debtList[i] -= curDebt #backtrack cleanup
                    path.pop()

                    if curDebt + curAttempResolvingDebt == 0:
                        break
            return minVal
        
        minVal = backtracking(0, debtList, [])
        #print(best_path)
        return best_path
    
sol = Solution()
print(sol.minTransfers([[0,1,10],[2,0,5]]))
print(sol.minTransfers( [[0,1,10],[1,0,1],[1,2,5],[2,0,5]]))