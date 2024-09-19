# Solved in 15 min but kinda tripped up alot
# I think its possible with one hashmap, but i used 2 to not be clever
# Neet code solution used 2 hashmaps

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        sList = s.split(' ')
        print(sList)

        if len(sList) != len(pattern):
            return False

        hashMap = {}
        reverseHashMap = {}
        for i, e in enumerate(pattern):

            if e in hashMap and hashMap[e] != sList[i]:
                return False
            elif sList[i] in reverseHashMap and reverseHashMap[sList[i]] != e:
                return False
            else: # new thing
                hashMap[e] = sList[i]
                reverseHashMap[sList[i]] = e
                

        print(hashMap)
        print(reverseHashMap)
        return True
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.wordPattern("abba", "dog cat cat dog")) # true
    print(sol.wordPattern("aaaa", "dog cat cat dog")) # false
    print(sol.wordPattern("abba", "dog dog dog dog")) # false
    print(sol.wordPattern("abc", "dog cat dog")) # false