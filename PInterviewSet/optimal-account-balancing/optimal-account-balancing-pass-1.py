from typing import List

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        debt = {}
        for t in transactions:
            fromPerson, toPerson, val = t[0], t[1], t[2]
            if not fromPerson in debt:
                debt[fromPerson] = 0
            debt[fromPerson] -= val

            if not toPerson in debt:
                debt[toPerson] = 0
            debt[toPerson] += val

        debtList = []
        for personKey in debt:
            debtList.append(debt[personKey])
        print(debtList)


        def backtracking(k, debtList):
            if k == len(debtList): # base case, we made it to the end
                return 0
            
            cur = debtList[k]
            if cur == 0: # nothing to settle, next
                return backtracking(k+1, debtList)

            minVal = float('inf')
            for i in range(k+1, len(debtList)):
                curItrateDebt = debtList[i]
                if cur * curItrateDebt < 0: #i guess its like neg * neg is not good, pos * pos is not good
                    debtList[i] = curItrateDebt + cur
                    curRet = 1+backtracking( k + 1,debtList)
                    minVal = min(minVal, curRet)
                    debtList[i] = curItrateDebt # backtracking

                    if cur + curItrateDebt == 0:
                        break
            return minVal

        ret = backtracking(0, debtList)
        print(ret)
        return ret
    
sol = Solution()