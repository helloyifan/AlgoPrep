# Spent 50 minutes, one oversight is [[a,a]] and we look for aaa, we cant use a,a again
# I think WHEN WE BUILD THE CHILDREN WE NEED TO USE RI, CI INSTEAD OF char

class Trie():
    def __init__(self, letter):
        self.letter = letter
        self.children = []

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        self.rowLen = len(board)
        self.colLen = len(board[0])

        self.dictOfLetters = {}

        self.createTrieNodeForEveryone(board)
        self.buildGraph(board)
        ret = self.buildResult(words)
        return ret
    
    def createTrieNodeForEveryone(self, board):
        for row in board:
            for colLetter in row:
                if colLetter not in self.dictOfLetters:
                    self.dictOfLetters[colLetter] = Trie(colLetter)

        self.trieHead = Trie(' ')
        for letter in self.dictOfLetters:
            self.trieHead.children.append(letter) #This trie is not like many levels, it only had the string letter as children

        return

    # Build a graph thats a trie of each other
    def buildGraph(self, board):
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        for ri, row in enumerate(board):
            for ci, colLetter in  enumerate(row):
                
                for dir in dirs:
                    nextRi = ri + dir[0]
                    nextCi = ci + dir[1]
                    
                    if ((0 <= nextRi < self.rowLen) and 
                        (0 <= nextCi < self.colLen)):
                        nextLetter = board[nextRi][nextCi]
                        self.dictOfLetters[colLetter].children.append(nextLetter)
        
        return
    
    def buildResult(self, words):
        ret = []
        for word in words: 
            if (self.findWord(word)):
                ret.append(word)
        return ret

    def findWord(self, word):
        letter = word[0]
        word = word[1:]
        trieNode = self.trieHead
        while letter in trieNode.children:
            if len(word) == 0:
                return True
            trieNode = self.dictOfLetters[letter]
            letter = word[0]
            word = word[1:]
            

        return False # shouild be impossible to hit


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

    # board_2 = [
    #     ["a","b"],
    #     ["c","d"]
    # ]
    
    # words_2 = ["abcb", 'a']
    # print(sol.findWords(board_2, words_2))

    # board_3 = [
    #     ["a","a"],
    # ]
    
    # words_3 = ["aaa"]
    # print(sol.findWords(board_3, words_3))