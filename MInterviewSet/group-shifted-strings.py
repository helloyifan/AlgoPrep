# Notes: A very confusing question
# A,B,C has a difference of [1,1,1], we want to use the tuple(unmutable hask key) (1,1,1):['abc', 'bcd', 'xyz']
# Note when calculating the difference between letes don't forget to %26 because of alphabet length

# TC: O(m*n) where m is the number of string s and n is the average length of string
# SC: for dd, we have g - different groups, storing m string, 
# However, we cannot have more groups then we have m, so space time is O(m)

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        dd = defaultdict(list)
        for string in strings: # O(m) where n is number of string
            currentShift = []

            for i, c in enumerate(string): # O(n) where m is the avgerage length of string
                curLetter, nextLetter = None, None
                if i < len(string) -1:
                    curLetter, nextLetter = ord(string[i]), ord(string[i+1])
                elif i ==  len(string) -1:
                    curLetter, nextLetter = ord(string[i]), ord(string[0]) #Wrap around
                currentShift.append((curLetter-nextLetter) %26)

            key = tuple(currentShift)
            dd[key].append(string)
        
        ret = []
        for key in dd:
            ret.append(dd[key])
        print(dd)
        return ret