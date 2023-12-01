class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1, w2 = '', ''
        for w in word1:
            w1 += w
        for w in word2:
            w2 += w
        return w1 == w2

sol = Solution()
word1 = ["ab", "c"] 
word2 = ["a", "bc"]
print(sol.arrayStringsAreEqual(word1, word2))