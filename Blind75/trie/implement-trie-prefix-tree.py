# I enjoyed doing this question, it took 30min, i probably could improve this code

class Trie(object):

    head = None
    def __init__(self):
        self.children = {}
        self.letter = None
        self.end = False

        return 

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """

        if self.head == None:
            self.head = Trie()
        
        self.insert_helper(word, self.head)
        return


    def insert_helper(self, word, node):
        if len(word) <= 0:
            node.end = True
            return

        char = word[0]
        if char not in node.children:
            node.children[char] = Trie()
            node.children[char].letter = char

        self.insert_helper(word[1:], node.children[char])
        return

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if self.head == None:
            return False

        return self.search_helper(word, self.head)
    
    def search_helper(self, word, node):
        if len(word) <= 0:
            return node.end #maybe alternatively we can instert None to children

        char = word[0]
        if char not in node.children:
            return False
        else:
            return self.search_helper(word[1:], node.children[char])
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        if self.head == None:
            return False

        return self.startsWith_helper(prefix, self.head)
    
    def startsWith_helper(self, prefix, node):
        if len(prefix) <= 0:
            return True

        char = prefix[0]
        if char not in node.children:
            return False
        else:
            return self.startsWith_helper(prefix[1:], node.children[char])
        

    def printTrie(self):
        currentHead =  self.head
        while currentHead != None:
            print(currentHead.letter)
            firstKey = next(iter(currentHead.children))
            currentHead = currentHead.children[firstKey]



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
        
if __name__ == '__main__':
    trie = Trie()
    # trie.insert("apple")
    # # trie.printTrie()
    # print(trie.search("apple"))   # return True
    # print(trie.search("app"))    # return False
    # print(trie.startsWith("app")) # return True
    # trie.insert("app")
    # print(trie.search("app"))    #return True

    print(trie.search("a"))