# Notes

#  [[0,1,10],[1,0,1],[1,2,5],[2,0,5]]

#  | 0, 1, 2
# -------------
# 0|    10             
# 1| 1      5        
# 2| 5
# 
# This means that if 2 pays 0 five,  then  0 has to pay 1 five less, if 1 pays 2 five (which it does)            
# This sounds like back tracking, but idk how to implement
# But maybe this idea is fucking retarded

# Another more  clever idea is to track debt
# One transcation means two changes for from and to person

# 0| 10 -1 -5 = 4
# 1| -10 +1 +5 = -4
# 2| -5 + 5 = 0
from typing import List
from collections import defaultdict

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        # pre-process (simplify owning)
        debt = {} # positive debt mean value owing
        for t in transactions:
            fromPerson, toPerson, val= t[0], t[1], t[2]

            if not fromPerson in debt:
                debt[fromPerson] = 0
            debt[fromPerson] += val

            if not toPerson in debt:
                debt[toPerson] = 0
            debt[toPerson] -= val

        debtList = []
        # preproecss to list
        for key in debt:
            debtVal = debt[key]
            if debtVal != 0:
                debtList.append(debtVal)

        print(debtList)

        #backtracing to get global min numbe rof transcatiosn
        # once current account + new account < 0, then we can perform next transcation
        def backtracking(k, debtList):
            if k == len(debtList)-1:
                return 0
            
            if debtList[k] == 0:
                return backtracking(k+1, debtList)

            minVal = float('inf')
            for i in range(k+1, len(debtList)):
                
                if debtList[i] * debtList[k] < 0: # pos * neg number 
                    debtList[i] += debtList[k]
                    minVal = min(minVal, 1+ backtracking(k+1, debtList))
                    debtList[i] -=  debtList[k]

            return minVal

        if len(debtList) == 0:
            return 0
        

        ret = backtracking(0, debtList)
        print(ret)
        return ret
    

sol = Solution()

sol.minTransfers([[0,1,10],[2,0,5]]) # 2
sol.minTransfers( [[0,1,10],[1,0,1],[1,2,5],[2,0,5]]) # 1
sol.minTransfers([[0,1,1],[1,2,1],[2,0,1]]) # 0