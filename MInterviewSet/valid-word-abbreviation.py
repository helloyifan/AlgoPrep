# Notes: Make sure to walk through code
# TC: O(n)
# SC: O(1)
class Solution:
    # Conditions,
    # non-empty substrings
    # non-adjacenet
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        wordI, abbrI = 0, 0

        while wordI < len(word):
            if abbrI > len(abbr) -1:
                return False
            
            elif word[wordI] == abbr[abbrI]:
                wordI +=1
                abbrI +=1

            elif abbr[abbrI].isnumeric():
                if abbr[abbrI] == '0':
                    return False

                wholeNumber, newAbbrIndex = self.findWholeNumberHelper(abbr, abbrI)
                # Still fits check
                if len(word) < wordI + wholeNumber:
                    return False
                
                wordI = wordI + wholeNumber
                abbrI = newAbbrIndex

            elif word[wordI] != abbr[abbrI]:
                return False
        
        # We didnt make it to the end of the Abbreviation
        if abbrI < len(abbr):
            return False
        
        return True
    
    # This will handle the non-adjacent part
    def findWholeNumberHelper(self, word, i):
        curI = i
        while curI < len(word) and word[curI].isnumeric():
            curI += 1
        return int(word[i:curI]), curI

sol = Solution()
print(sol.validWordAbbreviation("internationalization", "i12iz4n")) # True
print(sol.validWordAbbreviation("substitution", "sub0stitution")) # False (empty substring)
print(sol.validWordAbbreviation("substitution", "sub01stitution")) # False (no leading zero)
print(sol.validWordAbbreviation("s", "s0")) # False 
print(sol.validWordAbbreviation("ss", "ss")) # True 
print(sol.validWordAbbreviation("ss", "2")) # True?
print(sol.validWordAbbreviation("ss", "s1")) # True?


print(sol.validWordAbbreviation("apple", "a2e")) # False
print(sol.validWordAbbreviation("hi", "1")) # False

## Testing my helpr
#print(sol.findWholeNumberHelper("sub0stitution", 3)) # prin0 