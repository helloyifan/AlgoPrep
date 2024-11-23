# Time Complexity
# O(2^n) Since every character can be in a partiton or start of a new one
# Is pali will be O(n)
# Total is O(n*2^n)

# Space Complexity
# O(n) Stack memeory of n levels deep but each level we have substrings of sie O(n)
# O(n*n) = O(n^2)
from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def dfs(curS):
            if curS == "":
                return [[]]
            listOfRetProcessing = []

            for i in range(1, len(curS)+1):
                frontOfCurS = curS[:i]
                backOfCurS = curS[i:]

                if self.isPali(frontOfCurS):
                    tempRet = dfs(backOfCurS)
                    for r in tempRet:
                        listToAdd = [frontOfCurS]
                        listToAdd.extend(r)
                        listOfRetProcessing.append(listToAdd)
                        
            return listOfRetProcessing

        finRet = dfs(s)
        print(finRet)
        return finRet
        
    def isPali(self, s):
        if s == "":
            return True
        f, b = 0, len(s)-1
        
        while f < b:
            if s[f] != s[b]:
                return False
            f+=1
            b-=1
        return True

sol = Solution()
#sol.partition("aab")
sol.partition("cdd")

#print(sol.isPali("aa"))