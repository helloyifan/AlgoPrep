# Attempt 1, spend 30 minutes but i think i need to go i, i+1 i was going i-1, i
# Attempt 2. spend 20 minute still failed,.
# Attempt 3. Spend 30 more min and still failed (My answer is simliar to the correct answer, i just cant logically write it yet)
# Attempt 4. I was really close but did have to refer to solution
class Solution:
    def numDecodings(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        dp = {} # {sIndex: fiboncacci value}
        dp[len(s)] = 1
        for i in range(len(s) -1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
                
            if (i+2) in dp:
                if s[i] == '1' or ( s[i] == '2' and s[i+1] in '0123456'):
                    dp[i] += dp[i+2]
        # print(dp)
        return dp[0]


if __name__ == '__main__':
    s = Solution()
    # print(s.numDecodings('11106'))
    # print(s.numDecodings('121'))
    # print(s.numDecodings('01'))
    # print(s.numDecodings('12'))
    # print(s.numDecodings('226'))
    print(s.numDecodings('06'))
    print(s.numDecodings('1201234'))