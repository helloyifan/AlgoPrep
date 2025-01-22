from typing import List
import heapq

class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.heap = []

    def setOccurance(self, occurance):
        self.occurance = occurance

class Trie:
    root = None

    def __init__(self):
        self.root = TrieNode('')

    def addSentence(self, sentence, time):
        cur = self.root
        
        for c in sentence:
            newNode = None
            if not c  in cur.children:
                newNode = TrieNode(c)
            else:
                newNode = cur.children[c]

            self.manageNodeLevelHeap(cur.heap, sentence, time)
            cur.children[c] = newNode
            cur = newNode

        # At the last node add the occurance
        # cur.setOccurance(time)
        self.manageNodeLevelHeap(cur.heap, sentence, time)            
        
        return
    
    def manageNodeLevelHeap(self, heap, sentence, time):
        newVal = (time, sentence)

        if len(heap) == 3:
            oldVal = heapq.heappop(heap)
            oldValTime, oldValSentence = oldVal[0], oldVal[1]
            
            if oldValTime == time:
                # If the time value is the same, compare lexigraphically
                if oldValSentence < sentence:
                    heapq.heappush(heap, oldVal)
                else:
                    heapq.heappush(heap, newVal)
            elif oldValTime < time:
                heapq.heappush(heap, oldVal)
            else:
                heapq.heappush(heap, newVal)
        else:
            heapq.heappush(heap, newVal)

    def getTimes(self, sentence):
        cur = self.root
        for c in sentence:
            if not c in cur.children:
                return []
            
            cur = cur.children[c]

        ret = []
        tempHeap = []
        while len(cur.heap) > 0:
            t = heapq.heappop(cur.heap)
            ret.append(t[1])
            heapq.heappush(tempHeap, t)

        cur.heap = tempHeap        
        ret.reverse()
        return ret

class AutocompleteSystem:
    contentMap = {}
    def __init__(self, sentences: List[str], times: List[int]):
        for index in range(len(sentences)): 
            self.contentMap[sentences[index]] = times[index]

        self.reIndexEveryting()
        return

    def reIndexEveryting(self):
        self.trie = Trie()
        for key in self.contentMap:
            self.trie.addSentence(key, self.contentMap[key])
        return

    curSearchSentence = ''
    def input(self, c: str) -> List[str]:
        ret = []
        if c == '#':
            if self.curSearchSentence in self.contentMap:
                self.contentMap[self.curSearchSentence] += 1
            else:
                self.contentMap[self.curSearchSentence] = 1

            self.curSearchSentence = ''
            self.reIndexEveryting()
        else:
            self.curSearchSentence += c
            ret = self.trie.getTimes(self.curSearchSentence)

        print(ret)
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
