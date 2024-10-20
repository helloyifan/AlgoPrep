# Spent 35 mins and its pretty close imo,
# But ther vay we are removing from del adjlist is incorrect, its causing it to give differnt results on the same input

# Removed the use of del adjlist infavor of viisted
# ran into the case with with unconnected graphs not being accounted for
from typing import List
from collections import defaultdict
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = defaultdict(set)

        firstLetter = words[0][0]
        uniqueLetters = set()
        for word in words:
            for c in word:
                if c not in uniqueLetters:
                    uniqueLetters.add(c)

        for wordIndex in range(len(words)-1): # -1 so we dont consider last word (noting comes after it...)
            curWord = words[wordIndex]
            remainingList = words[wordIndex+1:]

            # Pretty complicated
            # but for each word, we want to evaluate the words that follow
            for afterWord in remainingList:
                # Based on the letter index of cur word
                # find at which point the cur word is greater then the afterWord
                for i in range(len(curWord)):
                    # If the afterword is too short, just skip this word
                    if i >= len(afterWord):
                        break
                    # if the letter is a match keep going
                    if curWord[i] == afterWord[i]:
                        continue
                    #if the letters dont match, track and skip the word after
                    else:
                        adjList[curWord[i]].add(afterWord[i])
                        break

        #print(adjList)

        def dfs(node, result, visited):
            if len(visited) == len(uniqueLetters) -1 : #-1 bcuz we are not account for words[0][0]
                return True # whole adjlist was added

            visited.append(node)
            childrenSet = adjList[node]
            children = list(childrenSet)
            #del adjList[node]

            for child in children:
                # Skip if we already been
                if child in visited:
                    continue

                tempRet = dfs(child, result, visited)
                if tempRet == True:
                    result.append(child)
                    return True

            # Failed to add everything, add back what was removed
            #adjList[node] = childrenSet
            del visited[-1]
            return False
        

        backWardResult = []
        visited = []
        valid = dfs(firstLetter, backWardResult, visited)

        result = -1
        if valid == True:
            backWardResult.append(firstLetter)
            result = backWardResult[::-1]
            result = "".join(result)

        print(result)
        return result
    
sol = Solution()
#sol.foreignDictionary(["hrn","hrf","er","enn","rfnn"])
#sol.foreignDictionary(["z", "o"])


#sol.foreignDictionary(["wrt","wrf","er","ett","rftt"]) # wertf
#sol.foreignDictionary(["abc","bca","cab"]) # abc
sol.foreignDictionary(["abc","bcd","cde"]) # edabc
