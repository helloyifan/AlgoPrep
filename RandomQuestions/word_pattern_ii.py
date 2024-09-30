# Solution: 
# https://leetcode.ca/2016-09-16-291-Word-Pattern-II/

# Spent 20 mins the first time and got confused,
# Watched video and will try again now
# 
# Watch video agan abefore retrying https://www.youtube.com/watch?v=W9ohcDTkUko&ab_channel=XianZhang

# Managed to get the cheated Sol in 15mins, should retry
class Solution:
    def cheatedSol(self, pattern: str, s: str) -> bool:
        pd = {}
        sd = {}

        def helper(p, s , pIndex, sIndex): 
            # Base case
            if len(p) == pIndex and len(s) == sIndex:
                return True
            
            if len(p) == pIndex or len(s) == sIndex:
                return False
            
            currentPattern = p[pIndex]  # Fix: Get the character in the pattern, not the index
            insertFlag = False
            
            for currentStringIndex in range(sIndex + 1, len(s) + 1):  # Adjust range to include more possibilities
                currentString = s[sIndex: currentStringIndex]  # Fix slicing to include correct substring

                # Check if the current pattern and string are consistent with previous mappings
                if currentPattern in pd and pd[currentPattern] != currentString:
                    continue
                if currentString in sd and sd[currentString] != currentPattern:
                    continue
                
                # If there's no mapping yet, set one
                if currentPattern not in pd and currentString not in sd:
                    pd[currentPattern] = currentString
                    sd[currentString] = currentPattern
                    insertFlag = True

                # Recursively check the next part of the pattern and string
                if helper(p, s, pIndex + 1, currentStringIndex):  # Move sIndex by the length of the matched substring
                    return True
                
                # Clean up after failed attempt
                if insertFlag:
                    del pd[currentPattern]
                    del sd[currentString]

            return False

        # Start the recursion
        return helper(pattern, s, 0, 0)
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.wordPatternii("abab", "redblueredblue")) # true
    # print(sol.wordPatternii("aaaa", "asdasdasdasd")) # true
    # print(sol.wordPatternii("aabb", "xyzabcxzyabc")) # false

'''
# Notes:

p maps to s

'''