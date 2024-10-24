# Spent 40 mins and it passed
# Not sure if i totally understand it tbh, its more so studying neetcode so much biases me
from typing import List
from collections import defaultdict
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = {}

        #uniqueLetter = set()
        for word in words:
            for c in word:
                # uniqueLetter.add(c)
                adjList[c] = set()
        
        for i in range(len(words)-1):
            curWord = words[i]
            remainingWords = words[i+1:]

            for afterWord in remainingWords:
                #samePrefix = True
                for i, c in enumerate(curWord):
                    # There is no index i such that a[i] != b[i] and a.length < b.length.

                    if i >= len(afterWord):
                        # If we hit this condition, this means that afterword
                        # must of shared the same prefix as beforeword, and afterowrd ran out of characters
                        # In means that in the input is invalid (a.length > b.length)
                        return ""
                    elif curWord[i] == afterWord[i]:
                        continue
                    else:
                        adjList[curWord[i]].add(afterWord[i])
                        break

        print(adjList)
        
        visited = {}
        result = []
        def dfs(node):
            if node in visited:
                # Return true if we have been there b4 in current scope
                # Return false if we havnt been there in current scope, but been there in prev
                    # No need to revisit children
                return visited[node] 

            # If we have never visited it b4, add it to current scope
            visited[node] = True
            childen = adjList[node]
            for child in childen:
                curRet = dfs(child) # if we been there b4 then stop
                if curRet == True:
                    return True

            visited[node] = False
            result.append(node)

        for key in list(adjList.keys()):
            curRet = dfs(key)
            if curRet == True: # if from the top level, we been there b4, then input is invalid
                return ""

        result = result[::-1]
        return "".join(result)



sol = Solution()
#print(sol.foreignDictionary(["hrn","hrf","er","enn","rfnn"]))
#print(sol.foreignDictionary(["wrtkj","wrt"])) # shold be ""
print(sol.foreignDictionary(["abc","bcd","cde"]))#edabc










