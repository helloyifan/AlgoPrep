from collections import defaultdict 

class Solution():
    def group_anagrams(self, strs):
        defaultDict = defaultdict(lambda: [])
        for str in strs:
            listOfSortedChars = sorted(str)
            key = ''.join(listOfSortedChars)
            defaultDict[key].append(str)
        
        ret = []
        for strList in defaultDict:
            ret.append(defaultDict[strList])
        return ret

if __name__ == "__main__":

    s = Solution()
    print(s.group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(s.group_anagrams([""]))
    print(s.group_anagrams(["a"]))