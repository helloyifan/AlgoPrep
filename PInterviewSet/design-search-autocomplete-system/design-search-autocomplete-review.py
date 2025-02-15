from typing import List


class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.child = {}
        self.sentence = None
        self.score = None

class Trie:
    def __init__(self):
        self.head = TrieNode('')
        self.dummy = self.head
    
    def add(self, sentence, score):
        head = self.head
        for c in sentence:
            if not c in head.child:
                head.child[c] = TrieNode(c)
            head = head.child[c]

        head.sentence = sentence
        head.score = score

    def get(self, sentence):
        head = self.head
        for c in sentence:
            if not c in head.child:
                # nothing to return
                return []
            else:
                head = head.child[c]

        # Once we found the point up to sentence, do dfs to get all words
        ret = []
        def dfs(node):
            if node.sentence != None:
                ret.append((node.score, node.sentence))
                return
            
            for key in node.child:
                dfs(node.child[key])
            return
        
        dfs(head)
        return ret

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Trie()
        self.curInputWord = ''


        n = len(sentences)
        for i in range(n):
            self.trie.add(sentences[i], times[i])
        return
    

    def input(self, c: str) -> List[str]:
        if c != "#":
            self.curInputWord += c
            ret = self.trie.get(self.curInputWord)
            ret = self.magicTopThreeSort(ret)

            print(ret)
        return
    
    def magicTopThreeSort(self, ret):
        ret.sort(key=lambda x: (-x[0], x[1]) ) #magic sort, first by descending nums, then by lexigraphical
        return ret[:3] # top 3 only

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)

sol = AutocompleteSystem(["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2])
sol.input('i')
sol.input(' ')
sol.input('a')
# sol.input('#')
# sol.input('i')
# sol.input(' ')
# sol.input('a')
# sol.input('#')
# sol.input('i')
# sol.input(' ')
# sol.input('a')
# sol.input('#')
