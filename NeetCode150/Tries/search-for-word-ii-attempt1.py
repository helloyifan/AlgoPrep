# Spent an hour but this solution is incorrect, its too slow
# The correct solution should rely on building a trie from the words
# And explore each cell of the board with  DFS to see what words can be discovered
from typing import List

class TrieNode:

    def __init__(self, character):
        self.children = []
        self.character = character
        self.visited = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        lenR = len(board)
        lenC = len(board[0])
        trieMatrix = [[None for _ in range(lenC)]  for _ in range(lenR)]
        
        # Copy the board to be Trie node per board
        trieHead = TrieNode("_")
        for row in range(lenR):
            for col in range(lenC):
                newTrieNode = TrieNode(board[row][col])
                trieMatrix[row][col] = newTrieNode
                trieHead.children.append(newTrieNode)

        # Make sure the trie nodes point to each other
        dirs = [(0,1),(0,-1),(-1,0),(1,0)]
        for row in range(lenR):
            for col in range(lenC):
                curTrieNode = trieMatrix[row][col]
                for d in dirs:
                    newRow = row + d[0] 
                    newCol = col + d[1]
                    if 0 <= newRow < lenR and 0 <= newCol < lenC:
                        curTrieNode.children.append(trieMatrix[newRow][newCol])

        # Traverse!
        def dfs(trieNode, remainingWord):
            if trieNode.visited == True and trieNode.character != "_":
                return False

            trieNode.visited = True
            if remainingWord == "":
                return True
            curLetter = remainingWord[0]
           
            remainingWord = remainingWord[1:]
            for childNode in trieNode.children:
                if childNode.character == curLetter:
                    temp = dfs(childNode, remainingWord)
                    if temp == True:
                        return True
            
            trieNode.visited = False
            return False
        finRet = []
        for word in words:
            ret = dfs(trieHead, word)
            if ret == True:
                finRet.append(word)
            self.resetVisited(trieMatrix)

        print(finRet)
        return finRet
    
    def resetVisited(self, trieMatrix):
        for row in trieMatrix:
            for trieNode in row:
                trieNode.visited = False
        return    

sol = Solution()
# board = [
#     ["a","b","c","d"],
#     ["s","a","a","t"],
#     ["a","c","k","e"],
#     ["a","c","d","n"]
# ]

# sol.findWords(board, ["bat","cat","back","backend","stack"]) # ["cat","back","backend"]


board2 = [
    ["x","o"],
    ["x","o"],
]

sol.findWords(board2, ["xoxo"]) 