from typing import List
from collections import defaultdict
# neetcode has a intuition where for graph problems
# you can do dfs but post order as a way to implmement topilogical sort
# This attempt is pretty bad
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = defaultdict(list)
        uniqueLetters = set()
        #1. build adj list
        for word in words:
            for i in range(len(word) -1):
                curLetter = word[i]
                nextLetter = word[i+1]
                if nextLetter not in adjList[curLetter]:
                    adjList[curLetter].append(nextLetter)

                if curLetter not in uniqueLetters:
                    uniqueLetters.add(curLetter)

                if nextLetter not in uniqueLetters:
                    uniqueLetters.add(nextLetter)

        for letter in uniqueLetters:
            adjList['_'].append(letter)

        
        print(adjList)


        def dfs(node, visited):
            if node not in adjList:
                return True

            children = adjList[node]
            del adjList[node]

            for child in children:
                tempRet = dfs(child, visited)
                if tempRet == True:
                    if child not in visited:
                        visited.append(child)


            # Add it back when we failed
            adjList[node] = children
            if child not in visited:
                visited.append(node)
            return False
        
        visited = []

        finRet = dfs('_', visited)

        print(visited)
        return finRet 
    
sol = Solution()
sol.foreignDictionary(["hrn","hrf","er","enn","rfnn"])