# Notes
# Discuss trade offs
# 1. Store At each level (for better TC, denormalized data worse SC,)
# 2. Store at root level, (slower/worse, TC better SC)

# Alternative designs
# Kept track of "time" in a dict instead of a trie
# Keep track of full sentence at every level instead of just root like mentioned above


# TC:
# Insertion: O(L)
#   Inserts a word character by character into the Trie. Each word has most L charcters

# Search: O(L + W log W)
    # Traverses the Trie to find the node corresponding to the prefix (O(L)).
    # Performs a DFS to collect words (O(W), where W is the total words under the prefix).
    # Sorts the results (O(W log W)).

# SC
# Overall Space Complexity: O(N * L) (Trie storage dominates).
    # If we insert N unique words, the worst case is storing N * L nodes.

# DFS Search Space Complexity: O(W) (temporary space for results).




from typing import List

class TrieNode:
    def __init__(self, character):
        self.character = character
        self.child = {}
        self.end = False
        self.times = None
        self.word = None
        return

class Trie:
    def __init__(self):
        self.head = TrieNode('')

    def addWord(self, word, times):
        cur = self.head

        for c in word:
            if not c in cur.child:
                cur.child[c] = TrieNode(c)

            cur = cur.child[c]            
        # Once we reach teh end, cur is the last node
        cur.end = True
        cur.times = times
        cur.word = word

        return
    
    # Band aid function to get times
    # Maybe instead we can track times in a another datastructure
    def getOccuranceOfWord(self, word):
        cur = self.head
        for c in word:
            if not c in cur.child:
                return 0
            cur = cur.child[c]

        if cur == None:
            return 0 
        if cur.times == None:
            print('wtf')
            return 0
        return cur.times

    def getWord(self, word):
        cur = self.head

        for c in word:
            if not c in cur.child:
                return [] # maybe should break

            cur = cur.child[c]

        # Once we found the point up to sentence, do dfs to get all words
        def dfs(node):
            if node == None:
                return
            
            ret = []
            if node.end == True:
                ret.append((node.times, node.word))

            for key, value in node.child.items():
                tempRet = dfs(value)
                ret.extend(tempRet)
            
            return ret

        allWords = dfs(cur)
        self.customSort(allWords)
        allWords = allWords[:3]
        return allWords
    
    def customSort(self, wordList): #magic sort, first by descending nums, then by lexigraphical
        # Sort by high priority to low, then sort by acending lexogrphical
        wordList.sort(key= lambda x: (-x[0], x[1]))
        return

class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.curInput = ''

        self.trie = Trie()
        for i in range(len(sentences)):
            sentence, time = sentences[i], times[i]
            self.trie.addWord(sentence, time)    
        return

    def input(self, c: str) -> List[str]:
        if c == '#':
            countOfCurrentSentence = self.trie.getOccuranceOfWord(self.curInput) + 1

            self.trie.addWord(self.curInput, countOfCurrentSentence ) #shouldnt be one lol
            self.curInput = '' # reset it
            return []
        else:            
            self.curInput = self.curInput + c
            ret = self.trie.getWord(self.curInput)
            # Post processing
            postPressedRet = []
            for r in ret:
                postPressedRet.append(r[1])
            
            #print(ret)
            print(postPressedRet)
            return postPressedRet
        

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)

sol = AutocompleteSystem(["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2])
sol.input('i')
sol.input(' ')
sol.input('a')
sol.input('#')
sol.input('i')
sol.input(' ')
sol.input('a')
sol.input('#')
sol.input('i')
sol.input(' ')
sol.input('a')
sol.input('#')
