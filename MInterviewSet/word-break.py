# TC: O(s*w*m) where s is length of string s and w is length of word dict where m is the avg size of word in wordDict
# SC: O(s) where s is length of string s for heap memory (call stack)

# Note adding memoization/DP doesnt change the time complexity
# Memoization dict would also be O(s) size

from typing import List
class Solution:
    def helperPrefix(self, prefix, s):
        lenOfPrefix = len(prefix)
        subStrOfS = s[:lenOfPrefix] #O(m) where m is the avg length of strhing

        if prefix != subStrOfS: #O(m) where m is the avg length of strhing
            return False
        return  True
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wouldFailDP= {} # fail fast

        def dfs(s, wordDict):
            if s in wouldFailDP:
                return False # fail fast, dont even try

            if s == "":
                return True
            
            for w in wordDict:
                if self.helperPrefix(w, s):
                    remainderOfString = s[len(w):]
                    tempRet = dfs(remainderOfString, wordDict)
                    # If any true is hit, surface that up
                    if tempRet == True:
                        return True

            wouldFailDP[s] = True
            return False
        
        ret = dfs(s, wordDict)
        print(ret)
        return ret
sol = Solution()
sol.wordBreak("leetcode", ["leet", "code"])
sol.wordBreak("applepenapple", ["apple", "pen"])
sol.wordBreak("catsandog", ["cats","dog","sand","and","cat"])