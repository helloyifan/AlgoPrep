# basically the post order traversal thing kind of blows my mind
# doesnt really make sense to me

# Also this solution doesnt properly account for " If the order is invalid, return an empty string"
# part of the problem

# I also question if im building the adj list correct

from typing import List
from collections import defaultdict
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList  = defaultdict(set)

        uniqueCharacters = set()
        for word in words:
            for c in word:
                uniqueCharacters.add(c)
                #adjList['_'].add(c)

        for wordIndex in range(len(words)-1):
            curWord = words[wordIndex]
            afterwords = words[wordIndex + 1:]
            for afterWord in afterwords:
                for i, c in enumerate(curWord):
                    if i >= len(afterWord):
                        break
                    if  c == afterWord[i]:
                        continue
                    if c != afterWord[i]:
                        adjList[c].add(afterWord[i])
                        break

        print(adjList)
        visited = {}

        def dfs(node, tempBackwardsResult):
            # If node is already in visited, this is invalid?
            if node in visited: 
                return visited[node]
            
            visited[node] = True
            children = list(adjList[node])
            for child in children:
                tempRet = dfs(child, tempBackwardsResult)
                # if invalid, just stop and back out?
                if tempRet == True:
                    return True

            visited[node] = False
            # Only add it to result
            # if non of the kids completed it 
            tempBackwardsResult.append(node) # this is crazy, this threw me off
            # ^ This is postorder part
            return False
        
        backwardsResult = []
        for key in uniqueCharacters:
            tempBackwardsResult = []
            ret = dfs(key, tempBackwardsResult)
            print(ret)
            for e in tempBackwardsResult:
                backwardsResult.append(e)

        forwardsResult = backwardsResult[::-1]
        forwardsResult =  "".join(forwardsResult)
        return forwardsResult



sol = Solution()
#print(sol.foreignDictionary(["hrn","hrf","er","enn","rfnn"]))
#print(sol.foreignDictionary(["z", "o"]))


#sol.foreignDictionary(["wrt","wrf","er","ett","rftt"]) # wertf
#print(sol.foreignDictionary(["abc","bca","cab"])) # abc

# invalid because of... reasons
print(sol.foreignDictionary(["wrtkj","wrt"])) # shold be ""