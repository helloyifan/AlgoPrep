class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        h, t = 0 , 0
        maxLen = 0
        while h < len(s):
            # Cond 1, if substring  doesn't contian duplicates
            h += 1
            subStr = s[t:h]
            subSet = set(subStr)
            # Cond 2, if substring does contian duplicates
            while len(subStr) > len(subSet):
                t += 1
                subStr = s[h:t]
                subSet = set(subStr)
            # Update ret only if subStr is valid
            maxLen = max(maxLen, len(subStr))

        return maxLen
if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring('abcabcbb'))

    print(s.lengthOfLongestSubstring('bbbbb'))

    print(s.lengthOfLongestSubstring('pwwkew'))

    print(s.lengthOfLongestSubstring(''))