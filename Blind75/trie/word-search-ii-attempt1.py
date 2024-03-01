# Spent 1 hour 30 mins on it
# This got 21/65 tests passed but i dont believe this approach is correct,
# I dont think leetcode wants you to build a trie like a tree and have a new node each tiem we reach a new character
# This solution didnt scale
class Trie():
    def __init__(self, letter):
        self.letter = letter
        self.children = {} # {letter: Trie}


class Solution(object):

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        self.board = board
        self.numOfRow = len(board)
        self.numOfCol = len(board[0])


        trieHead = Trie(' ')
        self.makeBigTrie(trieHead)
        
        ret = []
        for word in words:
            wordFound = self.checkIfWordInTrie(trieHead, word)
            if wordFound:
                ret.append(word)
            
        return ret
        
    def checkIfWordInTrie(self, trieHead, word):
        if len(word) == 0:
            return True
        
        letter = word[0]
        remaingWord = word[1:]
        if letter in trieHead.children:
            return self.checkIfWordInTrie(trieHead.children[letter], remaingWord)
        return False

    def makeBigTrie(self, trieHead):
        for ri, row in enumerate(self.board):
            for ci, col in enumerate(row):
                visited = []
                self.insertIntoTrie(trieHead, ri, ci, visited)
            

    def insertIntoTrie(self, trieHead, ri, ci, visited):
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        letter = self.board[ri][ci]

        if (ri, ci) not in visited:
            visited.append((ri, ci)) # Not sure if this is suppose to go here

        curTrie = None
        if letter not in trieHead.children:
            curTrie = Trie(self.board[ri][ci])
            trieHead.children[letter] = curTrie
        else:
            curTrie = trieHead.children[letter]

        for dir in dirs:
            nextRi = ri + dir[0]
            nextCi = ci + dir[1]
            
            if nextRi >= 0 and nextRi < self.numOfRow:
                if nextCi >= 0 and nextCi < self.numOfCol:
                    if (nextRi, nextCi) not in visited:
                        self.insertIntoTrie(curTrie, nextRi, nextCi, visited[:])
        return
    

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

    board_2 = [
        ["a","b"],
        ["c","d"]
    ]
    
    words_2 = ["abcb", 'a']
    print(sol.findWords(board_2, words_2))


    #board_3 = [["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"]]
    #words_3 = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    # print(sol.findWords(board_3, words_3))

