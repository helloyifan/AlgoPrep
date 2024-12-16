# Notes: 
# Intuitvely, we would keep track a counter of each character t: and decrement the letter counts
# when we check, we iterate through the counters to make sure they are all 0
# Thats an additional O(n) making a total of O(n^2)

# Smarter way
# keep track of two dicts, one for counter, one for the maximum occurance of each character (requiredTotalCounter)
# in our code, if our counter[s[r]] ever matches the requiredTotalCounter[s[r]]
# we know that we met one requirement of "required"
# we maintain the required (count it down) when we move R
# count it up when we move L
# When required is 0. we know we have a valid min answer

# TC: O(s+t) : O(t) for building out datastrucurree, O(s) for sliding window algorithm where we process each letter at most twice
# SC: O(t) : O(t) as the size of the dictionary grows proptional to size of t

from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r = 0, 0
        charCounter = {} #running character counter 
        requiredTotalCounter = {} # will be used to decide whether or not pointer should be moved
        # by matching it with charCounter

        for c in t:
            if c not in requiredTotalCounter: 
                requiredTotalCounter[c] = 0
                charCounter[c] = 0 # just initalize charcounter, we use it later
            requiredTotalCounter[c] += 1    
        
        required = len(requiredTotalCounter) # if this is 0, we have to move tail
        
        minSubString = None

        while r < len(s):
            # computer result?
            if s[r] in charCounter:
                charCounter[s[r]] += 1
                if charCounter[s[r]] == requiredTotalCounter[s[r]]:
                    required -= 1
            r+=1

            while required == 0:
                if required == 0:
                    if (minSubString == None) or len(minSubString) > len(s[l:r]):
                        minSubString = s[l:r]

                if s[l] in charCounter:
                    charCounter[s[l]] -=1
                    if charCounter[s[l]] < requiredTotalCounter[s[l]]: 
                        required += 1

                l+=1

        if minSubString == None:
            minSubString = ''

        return minSubString

            

sol = Solution()
print('ret: ', sol.minWindow("ADOBECODEBANC", "ABC"))
print('ret: ', sol.minWindow("bba", "ab"))