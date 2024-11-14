from collections import defaultdict
# Time comeplexity
# head for loop O(n)
# tails for loop O(n) but sine its sliding window we dont run for each iteration of head
# max check is O(1)
# Total O(n+n+1) = O(n)

# Space Complexity
# dd is O(m) where m is the number of unique characters

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        h, t = 0, 0
        dd = defaultdict(int)

        mostOccuringCharCount = 0
        mostOccuringChar = None

        finRet = 0
        while h < len(s):
            subStr = s[t:h+1]
            # Count most commonly occuring letter
            dd[s[h]] += 1
            if (mostOccuringCharCount < dd[s[h]]):
                mostOccuringCharCount = dd[s[h]]
                #mostOccuringChar = s[h]
            

            while t < len(s) and len(subStr) > mostOccuringCharCount + k:
                dd[s[t]] -=1
                subStr = s[h:t]
                if (mostOccuringCharCount < dd[s[t]]):
                    mostOccuringCharCount = dd[s[t]]
                    #mostOccuringChar = s[t]
                t += 1

            finRet = max(finRet, mostOccuringCharCount + k) #is mostOccuringCharCount + k the same as k lol
            h += 1
        
        finRet = min(finRet, len(s))
        print(finRet)

        return finRet


sol = Solution()
sol.characterReplacement("ABAB", 2) # 4
sol.characterReplacement("AABABBA", 1) # 4
sol.characterReplacement("AAAA", 2) # 4
sol.characterReplacement("ABAB", 0) # 1

'''
Notes:
given k = 1

A MC = A 
AA MC = A
AAB MC = A
AABA MC = A

AABAB MC = A, however len(subStr) > mc + k

ABAB MC = A, however len(subStr) > mc + k

BAB MC = B,

BABB MC = B

BABBA MC = B, however len(subStr) > mc + k
ABBA MC = A, howver len(subStr) > mc + k

BBA MC = B
'''