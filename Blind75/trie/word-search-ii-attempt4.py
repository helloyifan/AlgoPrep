# Attempt took 1:15mins
# I got really close but fundamentally the idea is still incorrect

from typing import List

class Trie:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.count = 1

class Solution:
    def insertWord(self, trie, word):
        if len(word) == 0:
            return
        letter = word[0]
        if letter in trie.children:
            trie.children[letter].count += 1
        else:
            trie.children[letter] = Trie(letter)

        self.insertWord(trie.children[letter], word[1:])
        return 

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        self.board = board
        self.maxRowIndex = len(board)
        self.maxColIndex = len(board[0])

        headTrie = Trie('/')
        headTrie.count -= 1 # When you create it its 1 by default


        for word in words:
            self.insertWord(headTrie, word)

        ret = []
        for ir, row in enumerate(board):
            for ic, col in enumerate(row):
                letter = col
                if letter in headTrie.children:
                    potentialWordFound = self.findWord(headTrie.children[letter], ir, ic, [])
                    print(potentialWordFound)
                    if potentialWordFound in words and potentialWordFound not in ret:
                        ret.append(potentialWordFound)
        return ret

    
    def findWord(self, trie, ir, ic, alreadyWalked):
        dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]

        alreadyWalked.append((ir, ic))
        trie.count -=1 # Really not sure about this

        prevLetters = ''
        for dir in dirs:
            newIr = ir + dir[0]
            newIc = ic + dir[1]

            if 0 <= newIr < self.maxRowIndex and 0 <= newIc < self.maxColIndex:
                if (newIr, newIc) not in alreadyWalked:
                    newLetter = self.board[newIr][newIc]
                    if newLetter in trie.children and trie.children[newLetter].count > 0:
                        prevLetters = self.findWord(trie.children[newLetter], newIr, newIc, alreadyWalked)

                        break
        
        curRet = trie.letter + prevLetters
        return curRet


if __name__ == '__main__':
    sol = Solution()
    board_1 = [
        ["o","a","a","n"],
        ["e","t","a","e"],
        ["i","h","k","r"],
        ["i","f","l","v"]
    ]
    words_1 = ["oath","pea","eat","rain"]
    print(sol.findWords(board_1, words_1))



    # board_4 = [
    #     ["o","a","b","n"],
    #     ["o","t","a","e"],
    #     ["a","h","k","r"],
    #     ["a","f","l","v"]
    # ]
    # words_4 = ["oa","oaa"]
    # print(sol.findWords(board_4, words_4))


    # board_5 = [
    #     ["a","a","a","a","a","a","a","a","a","a","a","a"],
    #     ["a","a","a","a","a","a","a","a","a","a","a","a"],
    #     ["a","a","a","a","a","a","a","a","a","a","a","a"],
    #     ["a","a","a","a","a","a","a","a","a","a","a","a"],
    #     ["a","a","a","a","a","a","a","a","a","a","a","a"],
    #     ["a","a","a","a","a","a","a","a","a","a","a","a"],
    #     ["a","a","a","a","a","a","a","a","a","a","a","a"],
    #     ["a","a","a","a","a","a","a","a","a","a","a","a"],
    #     ["a","a","a","a","a","a","a","a","a","a","a","a"],
    #     ["a","a","a","a","a","a","a","a","a","a","a","a"],
    #     ["a","a","a","a","a","a","a","a","a","a","a","a"],
    #     ["a","a","a","a","a","a","a","a","a","a","a","a"]
    # ]
    # words_5 = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    # print(sol.findWords(board_5, words_5))

    board_6 = [
        ["o","a","a","n"],
        ["e","t","a","e"],
        ["i","h","k","r"],
        ["i","f","l","v"]
    ]
    words_6 = ["oath","pea","eat","rain","hklf", "hf"]
    print(sol.findWords(board_6, words_6))
