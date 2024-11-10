class Solution:
    def checkValidString(self, s: str) -> bool:
        dp = {}
        def dfs(remainingS, openCounter):
            if (remainingS, openCounter) in dp:
                return dp[(remainingS, openCounter)]

            if remainingS == "":
                if openCounter == 0:
                    return True
                return False

            if openCounter < 0:
                return False
            
            curChar = remainingS[0]
            stringToPass = remainingS[1:]

            ret = False
            if curChar == "(":
                ret = ret or dfs(stringToPass, openCounter+1)
            elif curChar == ")":
                ret = ret or dfs(stringToPass, openCounter-1)
            elif curChar == "*":
                ret = ret or dfs(stringToPass, openCounter+1)   
                ret = ret or dfs(stringToPass, openCounter-1)
                ret = ret or dfs(stringToPass, openCounter) #To optimize at anytime if ret is true, return true butowell

            dp[(remainingS, openCounter)] = ret
            return ret
        
        finRet = dfs(s, 0)
        # print(dp)
        print(finRet)
        return finRet

sol = Solution()
sol.checkValidString("((**)") # true
sol.checkValidString("(((*)") # false
sol.checkValidString("((**)") # true