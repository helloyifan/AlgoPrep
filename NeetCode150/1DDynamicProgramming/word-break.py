# solved in 30 mins from intuition
# also sad, i solved this for google interview back in 2018
# Space: O(n^2) where n is length of s
    # incorrect, its O(2^n) If we assume every possible substring of s could be unique in the recursive calls, then dp could store up to  
# Time: O(n*m) where n is length of s and m is number of words
from typing import List
class Solution:

    # Problem is that we are doing BFS instead of DFS
    # When we find one answwerthats good its good
    def tooSlow(self, s: str, wordDict: List[str]) -> bool:
        q = [s] # store all the suffix ya?
 
        while len(q) > 0:
            curRemainingString = q.pop(0)
            for word in wordDict:
                if self.doesWordFit(curRemainingString, word):
                    suffix = curRemainingString[len(word):]
                    if len(suffix) == 0:
                        return True
                    q.append(suffix)


        return False
    
    def doesWordFit(self, s, word):
        wordLen = len(word)

        if wordLen > len(s):
            return False

        prefix = s[:wordLen]        
        if word == prefix:
            return True
        return False
    
    # Works needed to add memoization
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        def dfs(curRemainingString, wordDict):
            if curRemainingString in dp :
                return False

            if len(curRemainingString) == 0:
                return True
            for word in wordDict:
                if self.doesWordFit(curRemainingString, word):
                    suffix = curRemainingString[len(word):]
                    tempRet = dfs(suffix, wordDict)
                    if tempRet == True:
                        return True
                    
            # Set dp to avoid this
            dp[curRemainingString] = True
            
            return False
        

        finRet = dfs(s, wordDict)
        return finRet




sol = Solution()
# print(sol.wordBreak("neetcode", ['neet', 'code'])) # True
# print(sol.wordBreak("applepenapple", ['apple', 'pen', 'ape'])) # True "apple" "pen" "apple"
print(sol.wordBreak("catsincars",  ["cats","cat","sin","in","car"])) # False
