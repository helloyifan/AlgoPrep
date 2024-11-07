# This solution doesnt work at all
# Spent 35min on a solution on tuesday but it was totally wrong
# Spent 15min got recursion soliution
# recursiveNumDistinct:
    # Time Complexity: O(2^(s)) because 
    # Space Complexity: O(s) for stack (at most we go s levels deep)

# topDownDPnumDistinct:
    # Time Complexity: O(s*t) 
    # Space Complexity: O(s*t) for stack and 0(s*t) for dp

# bottomupDP todo:

class Solution:
    def recursiveNumDistinct(self, s: str, t: str) -> int:
        def dfs(i, remainingT):
            if i >= len(s) and remainingT != "":
                return 0
            if remainingT == "":
                return 1

            ret = 0            
            if (s[i] == remainingT[0]):
                ret += dfs(i+1, remainingT[1:])

            ret += dfs(i+1, remainingT)
            return ret

        finRet = dfs(0, t)
        print(finRet)
        return finRet
    
    def topDownDPnumDistinct(self, s: str, t: str) -> int:
        dp = {}

        def dfs(i, remainingT):
            if (i, remainingT) in dp:
                return dp[(i, remainingT)]

            if i >= len(s) and remainingT != "":
                return 0
            if remainingT == "":
                return 1

            ret = 0            
            if (s[i] == remainingT[0]):
                ret += dfs(i+1, remainingT[1:])

            ret += dfs(i+1, remainingT)
            dp[(i, remainingT)] = ret
            return ret

        finRet = dfs(0, t)
        print(finRet)
        return finRet
    
    def anotherSolutionThatsTooSlow(self, s: str, t: str) -> int:
        dp = [] #{ ("string", "sIndex") : true}
        dp.append('')
        for i in range(len(s)):
            tempDp = []
            while len(dp) > 0:
                c = dp.pop()
                curSChar = s[i]

                withNewChar = c[:] + curSChar
                
                if len(withNewChar) <= len(t) and withNewChar == t[:len(withNewChar)]: #First n letters match
                    tempDp.append(withNewChar)

                withOutnewChar = c[:]
                if len(withOutnewChar) <= len(t) and withOutnewChar == t[:len(withOutnewChar)]: #First n letters match
                    tempDp.append(c[:len(withOutnewChar)])
            dp = tempDp

        finRet = 0
        for i in dp:
            if i == t:
                finRet +=1
        # print(dp)
        # print(finRet)
        return finRet

sol = Solution()
sol.numDistinct("caaat", "cat") # 3
sol.numDistinct("xxyxy", "xy") # 5

sol.numDistinct("rabbbit", "rabbit") # 3

