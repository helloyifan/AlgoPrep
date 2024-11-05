# This solution doesnt work at all
# Spent 35min s
import copy
class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        breakDownS = []

        prevLetter = None
        prevLetterIndex = None
        for i, c in enumerate(s):
            if prevLetter == None:
                prevLetter = c
                prevLetterIndex = i
            
            elif prevLetter != c:
                breakDownS.append(s[prevLetterIndex:i])
                prevLetter = c
                prevLetterIndex = i
        
        breakDownS.append(s[prevLetterIndex:])

        print(breakDownS)

        # Attempting Recursive solution
        def dfs(breakDownS, i, remainingT):

            if remainingT == "":
                return 1
            if i >= len(breakDownS) and remainingT != "":
                return 0
            
            curSCharSet = breakDownS[i]
            curSChar = curSCharSet[0] # 0 bcuz all characters are teh same
            
            ret = 0
            if curSChar == remainingT[0]:
                tCopy = copy.deepcopy(remainingT)
                tCopy = tCopy[1:]

                ret = dfs(breakDownS, i+1,  tCopy)
                ret *= len(curSCharSet) # cur options

            ret += dfs(breakDownS, i+1, t)
            return ret
        
        finRet = dfs(breakDownS, 0, t)
        print(finRet)
        return finRet


sol = Solution()
# sol.numDistinct("caaat", "cat") # 3
# sol.numDistinct("xxyxy", "xy") # 5

sol.numDistinct("rabbbit", "rabbit") # 3

