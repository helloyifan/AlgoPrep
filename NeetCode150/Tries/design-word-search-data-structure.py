# Solved in 45mins
# it a bit weird to do the DFS inside a condiional, but i guess it makes sense

# Runtinme complexity:
# Add: Runtime is O(n)
# Search: Runtime is O(v^e) because we dont know which edge to pick so 
class TrieNode:
    def __init__(self, val):
        self.children = {}
        self.val = val
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.head = TrieNode('_')

    def addWord(self, word: str) -> None:
        curHead = self.head
        for c in word:
            if not c in curHead.children:
                curHead.children[c] = TrieNode(c)
            curHead = curHead.children[c]
        curHead.endOfWord = True

    def search(self, word: str) -> bool:

        def dfs(curHead, word):
            for i, c in enumerate(word):
                if c == '.':
                    for c2 in curHead.children:
                        newWord = c2 + word[i+1:]
                        tempRet = dfs(curHead, newWord)
                        if tempRet == True:
                            return True
                    return False
                elif c in curHead.children:
                    curHead = curHead.children[c]
                else:
                    return False

            return curHead.endOfWord
        
        curHead = self.head
        ret = dfs(curHead, word)
        return ret
    

# Test set case 1
# wordDictionary = WordDictionary()
# wordDictionary.addWord("day")
# wordDictionary.addWord("bay")
# wordDictionary.addWord("may")
# # print(wordDictionary.search("say"))  # return False
# # print(wordDictionary.search("day"))  # return True
# print(wordDictionary.search(".ay"))  # return True
# print(wordDictionary.search("b.."))  # return True

# Test set case 1
wordDictionary = WordDictionary()
wordDictionary.addWord("dog")
print(wordDictionary.search("d..."))  # 