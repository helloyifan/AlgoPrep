from typing import List

class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}

    def setOccurance(self, occurance):
        self.occurance = occurance

class Trie:
    def __init__(self):
        self.head = TrieNode('')

    def addSentence(self, sentence, occurance):
        cur = self.head

        for c in sentence:
            if not c in cur.children:
                cur.children[c] = TrieNode(c)
            child = cur.children[c]
            cur = child
        # At the end set the last trie node
        cur.setOccurance(occurance)


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Trie()

        # Preprocess sentence / times to be on datastruct
        # TC: O(n), SC: O(n)
        self.data = {}
        for i in range(len(sentences)):
           self.data[sentences[i]] =  times[i]

        # Write to trie
        # TC: O(n),
        for key in self.data:
            self.trie.addSentence(key, self.data[key])
        return

    curWord = ''
    def input(self, c: str) -> List[str]:
        if c == '#':
            if not self.curWord in self.data:
                self.data[self.curWord] = 1
            else:
                self.data[self.curWord] += 1

            self.trie.addSentence(self.curWord,  self.data[self.curWord])
            # Reset it 
            self.curWord = ''

        else:
            

        return


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)

sol = AutocompleteSystem(["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2])
sol.input('i')
sol.input(' ')
sol.input('a')
sol.input('#')
# sol.input('i')
# sol.input(' ')
# sol.input('a')
# sol.input('#')
