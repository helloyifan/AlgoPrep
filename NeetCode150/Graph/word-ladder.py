# Solved the neetcode test cases in 28mins, but failed LC test cases for taking too long
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = []
        
        def dfs(curWord, curVisited):
            #print(curWord)
            if curWord == endWord:
                curVisited.append(curWord)
                return (True, 1)

            nextSteps = self.validNextSteps(curWord, wordList)
            minV = float('inf')
            for i in nextSteps:
                if not i in curVisited:
                    curVisited.append(curWord)
                    copy = curVisited[:]
                    t = dfs(i, copy)
                    if t[0] == False:
                        curVisited.remove(curWord)
                    elif t[0] == True:
                        minV = min(minV, t[1])
            
            if minV != float('inf'):
                return (True, minV + 1)

            return (False, 0)
        
        finRet = dfs(beginWord, visited)
        print('---')
        print(finRet)
        return finRet[1]
    
    def validNextSteps(self, curWord, wordList):
        ret = []
        for word in wordList:
            diff = 0
            for i, e in enumerate(word):
                if word[i] != curWord[i]:
                    diff += 1
                
            if diff == 1:
                ret.append(word)
        return ret

sol = Solution()
sol.ladderLength("cat", "sag", ["bat","bag","sag","dag","dot"]) # 4
sol.ladderLength("cat", "sag", ["bat","bag","sat","dag","dot"]) # 0
sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]) # 5