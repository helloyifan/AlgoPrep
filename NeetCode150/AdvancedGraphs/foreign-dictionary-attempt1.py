from typing import List
from collections import defaultdict
# Tried for an hour, i think i have piecs that dont work individually or togehter.
# I dont think i understand the question still
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjDict = {}
        # Setup my datastrcutrue
        for wordIndex, word in enumerate(words):
            prevLetter = None
            for curLetter in word:
                if curLetter not in adjDict:
                    adjDict[curLetter] = {
                        "pointsTo": set(),
                        "score": 0
                    }
                
                if prevLetter != None:
                    adjDict[prevLetter]["pointsTo"].add(curLetter)
                
                adjDict[curLetter ]["score"] = wordIndex
                prevLetter = curLetter
        
        adjList = sorted(adjDict.items(), key=lambda x: x[1]["score"])
        groupedAdjList = defaultdict(list)

        for i in adjList:
            groupedAdjList[i[1]['score']].append(i)

        #self.printListHelper(adjList)

        # Topilogical sort
        # {
        #   node : [neighbor1, neighbor2]
        # }

        finalRet = ""
        for i in groupedAdjList:
            curListOfNodesToAdjList = {}
            buildingOutListOfEverything = []
            for oldKey in groupedAdjList[i]:
                letterKey = oldKey[0]
                curListOfNodesToAdjList[letterKey] = oldKey[1]["pointsTo"]
                buildingOutListOfEverything.append(letterKey)
            
            startingLetter = '_'
            curListOfNodesToAdjList[startingLetter] = buildingOutListOfEverything
            visited = []
            valid = self.dfs(startingLetter, visited, curListOfNodesToAdjList)

            if valid:
                print(visited)
                finalRet += visited
            else:
                print("invalid")
                finalRet = -1

        return finalRet
    # Top sort on {'r': {'n', 'f'}, 'n': {'n'}, 'f': {'n'}, '_': ['r', 'n', 'f']}
    def dfs(self, node, visited, curListOfNodesToAdjList):
        if len(curListOfNodesToAdjList) == 0:
            return True

        neighbors = curListOfNodesToAdjList[node]
        del curListOfNodesToAdjList[node]

        visited.append(node)
        for n in neighbors:
            tempRet = self.dfs(n, visited, curListOfNodesToAdjList)
            if tempRet == True:
                return True
        # I think we have to add it back
        curListOfNodesToAdjList[node] = neighbors[:] # copying to prevent polution i think
        visited.remove(node)

        return False

    def printDictHelper(self, adjDict):
        for k in adjDict:
            print(k, adjDict[k])
    
sol = Solution()
#sol.foreignDictionary(["z","o"]) #zo
#sol.foreignDictionary(["hrn","hrf","er","enn","rfnn"]) #hernf

# Testing my dfs top sort
visited =  []
sol.dfs("_", visited, {'r': {'n', 'f'}, 'n': {'n'}, 'f': {'n'}, '_': ['r', 'n', 'f']})
print(visited)