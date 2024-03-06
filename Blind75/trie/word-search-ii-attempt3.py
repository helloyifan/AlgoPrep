# Spent another 1 hour, the 'oaa' and 'oa' stuff tripped me up
# need to count occurance of each letter
class Trie():

    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        return
    
    def insertChild(self, letter):
        if letter in self.children:
            return self.children[letter]
        else:
            newTrieNode = Trie(letter)
            self.children[letter] = newTrieNode
            return newTrieNode

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """

        self.rootTrieNode = Trie(' ')
        self.maxRi = len(board)
        self.maxCi = len(board[0])

        self.insertWordsIntoTrie(words)
        

        finRet = []
        for ri, row in enumerate(board):
            for ci, col in enumerate(row):
                curLetter = board[ri][ci]
                if curLetter in self.rootTrieNode.children:
                    traversed = []
                    ret = self.matchWord(ri, ci, board, self.rootTrieNode.children[curLetter], '', traversed)
                    if ret != None:
                        finRet.append(ret)

        return finRet
    
    def matchWord(self, ri, ci, board, trieNode, ret, traversed):
        ret = ret + trieNode.letter
        traversed.append((ri, ci))

        if not trieNode.children:
            return ret
        
        if board[ri][ci] != trieNode.letter:
            return None


        dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        for dir in dirs:
            newRi = ri + dir[0]
            newCi = ci + dir[1]

            if (0 <= newRi < self.maxRi and 0 <= newCi < self.maxCi):

                newLetter = board[newRi][newCi]
                if newLetter in trieNode.children and (newRi, newCi) not in traversed:
                    finRet = self.matchWord(newRi, newCi, board, trieNode.children[newLetter], ret, traversed)

                    if finRet != None:
                        return finRet



    def insertWordsIntoTrie(self, words):

        for word in words:
            trieHead = self.rootTrieNode
            for letter in word:
                trieHead = trieHead.insertChild(letter)
        return
    

if __name__ == '__main__':
    sol = Solution()
    # board_1 = [
    #     ["o","a","a","n"],
    #     ["e","t","a","e"],
    #     ["i","h","k","r"],
    #     ["i","f","l","v"]
    # ]
    # words_1 = ["oath","pea","eat","rain","oak"]

    # print(sol.findWords(board_1, words_1))

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

    board_4 = [
        ["o","a","b","n"],
        ["o","t","a","e"],
        ["a","h","k","r"],
        ["a","f","l","v"]
    ]
    words_4 = ["oa","oaa"]
    print(sol.findWords(board_4, words_4))
