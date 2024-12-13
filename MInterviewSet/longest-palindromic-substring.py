'''
5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Input: s = "babad"
Output: "bab"

Input: s = "cbbd"
Output: "bb"
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxPalindromeLength = float('-inf')
        maxPalindrome = (0, 0)
        for i in range(len(s)):
            singleResult = self.helperPalindromInOutChecker(s, i, i)
            if maxPalindromeLength < singleResult[1] - singleResult[0]:
                maxPalindromeLength = singleResult[1] - singleResult[0]
                maxPalindrome = singleResult

            doubleResult = self.helperPalindromInOutChecker(s, i, i+1)
            if maxPalindromeLength < doubleResult[1] - doubleResult[0]:
                maxPalindromeLength = doubleResult[1] - doubleResult[0]
                maxPalindrome = doubleResult

        print(maxPalindrome)  
        print(s[maxPalindrome[0]: maxPalindrome[1]+1]) # Convert back to string from pointers
        return s[maxPalindrome[0]: maxPalindrome[1]+1]

    def helperPalindromInOutChecker(self, s, l, r):
        #maxPalindromeLength = float('-inf') 
        maxPalindrome = (0,0)
        while l > -1 and r < len(s):
            if s[l] != s[r]:
                return maxPalindrome
            maxPalindrome = (l, r)
            l -= 1
            r += 1
        return maxPalindrome
# b
# palidons b

# a
# bab

#print(helperPalindromInOutChecker("babad", 1,1))
#print(helperPalindromInOutChecker("cbbd", 1,2))

# TC: helperPalindromInOutChecker: O(n) longestPalindrome for loop O(n) = O(n) Total O(n^2)
# SC: O(1) because maxPalindrome could be the most

longestPalindrome("babad")
longestPalindrome("cbbd")
