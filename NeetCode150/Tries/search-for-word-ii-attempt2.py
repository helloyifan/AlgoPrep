
from typing import List
# Different approach, built trie from Words
# Explored the graph to see which words in trie can be scanned

## Runtime Analysis
# Time Complexity:
# Build trie O(words*longestWordSize)
# DFS O(boardsize*4^(longestWordSize))
# Total: O(characterAndWords + boardsize*4^(longestWordSize))

# Space Complexity:
# Trie: O(words*longestWordSize)
# DFS: Deepest we will go is O(longestWordSize)
# Total: O(words*longestWordSize + longestWordSize) 
class TrieNode:

    def __init__(self, character):
        self.children = {}
        self.character = character
        self.endOfWord = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        lenR = len(board)
        lenC = len(board[0]) 
        dirs = [(0, 1),(0, -1),(-1, 0),(1,0)]

        # Write words to trie
        trieHead = TrieNode("_")
        for word in words:
            parentNode = trieHead
            for character in word:
                if not character in parentNode.children:
                    parentNode.children[character] = TrieNode(character)
                parentNode = parentNode.children[character]
            parentNode.endOfWord = True

        foundWords = set()
        def dfs(trieNode, r, c, path):
            if trieNode.endOfWord:
                foundWords.add(path)

            startingState =board[r][c]
            board[r][c] = '#' # To prevent from visited this node again for current word

            for dir in dirs:
                newR, newC = r+dir[0], c+dir[1]
                if 0 <= newR < lenR and 0 <= newC < lenC:
                    newChar = board[newR][newC]
                    if newChar in trieNode.children:
                        newPath = path + newChar
                        dfs(trieNode.children[newChar], newR, newC, newPath)
            
            board[r][c] = startingState 

            return

        for ir, r in enumerate(board):
            for ic, c in enumerate(r):
                startingChar = board[ir][ic]
                if startingChar in trieHead.children:
                    dfs(trieHead.children[startingChar], ir, ic, startingChar)

        print(list(foundWords))
        return list(foundWords)

sol = Solution()
board = [
    ["a","b","c","d"],
    ["s","a","a","t"],
    ["a","c","k","e"],
    ["a","c","d","n"]
]

sol.findWords(board, ["bat","cat","back","backend","stack"]) # ["cat","back","backend"]


# board2 = [
#     ["x","o"],
#     ["x","o"],
# ]

# sol.findWords(board2, ["xoxo"]) 


# board3 = [
#     ["a"],
# ]

# sol.findWords(board3, ["a"]) 