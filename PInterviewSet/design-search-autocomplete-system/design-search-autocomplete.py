# Notes: This solution is different from attempt1 where we maintain a heap for every node
# This solution uses less space as we dont do that, but has greater TC as we need to do full 
# DFS to explore every node in the tree once we match the prefix
# TC:
# SC:
from typing import List

class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.occurance = None
        self.sentence = None

    def setOccurance(self, occurance):
        self.occurance = occurance

    def setSentence(self, sentence):
        self.sentence = sentence


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
        cur.setSentence(sentence)

    def getSentenceFromPrefix(self, prefix):
        cur = self.head
        # Match up to prefix
        for c in prefix:
            if not c in cur.children:
                return []
            else:
                cur = cur.children[c]

        #dfs until u find everything
        ret = []
        def dfs(cur, ret):
            if cur == None:
                return 
            
            if cur.occurance != None:
                ret.append((cur.occurance, cur.sentence))
            
            for childKey in cur.children:
                child = cur.children[childKey]
                dfs(child, ret)

            return
        
        dfs(cur, ret)
        return ret


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Trie()
        self.curWord = ''

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

    def input(self, c: str) -> List[str]:
        ret = []
        finRet = []

        if c == '#':
            if not self.curWord in self.data:
                self.data[self.curWord] = 1
            else:
                self.data[self.curWord] += 1

            self.trie.addSentence(self.curWord,  self.data[self.curWord])
            # Reset it 
            self.curWord = ''
        else:
            self.curWord += c
            ret = self.trie.getSentenceFromPrefix(self.curWord)
            ret = self.helperTopIfSameOccuranceLexigraphicalOrder(ret)
            ret = ret[:3] # only care about top3 

            ## remove occurance from final output
            for r in ret:
                finRet.append(r[1])


        print(finRet)
        return finRet

    def helperTopIfSameOccuranceLexigraphicalOrder(self, ret):
        ret.sort(key=lambda x: (-x[0],  x[1])) # the reason why this fking works is wild
        # this looks like magic and it basically is, 
        # but -x[0] means we want to first sort this list of tuples by the occurance, however negative maks this a maxheap
        # so the result is we have a list of (occurance, sentence) first sorted by 

        # x[1] means we want to lexigraphically sort the sentence IN THE CASE WHERE THE OCCURANCES ARE THE SAME
        # so its kinda just a fluke this sorting works for this specifc question
        return ret

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
