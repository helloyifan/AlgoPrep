# This is an accepted solution
# Time complexity: O(m*n)
# Space complexity: O(m*n
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # text1 direction(v), text2 direction(>)
        dp = [[0]* (len(text2)) for i in range(len(text1))]
        
        
        for i1, t1 in enumerate(text1):
            for i2, t2 in enumerate(text2): # t2 being c of text2
                subSeqCount = 0 
                         
                if t2 == t1:
                    if i1>0 and i2>0:
                        subSeqCount = dp[i1-1][i2-1] + 1 #Attempt 2 the difference is this, adding the diagonal to the +1
                    else:
                        subSeqCount = 1
                else:
                    temp1 = dp[i1-1][i2] if i1 > 0 else 0
                    temp2 = dp[i1][i2-1] if i2 > 0 else 0
                    subSeqCount = max(temp1, temp2)
                
                dp[i1][i2] = subSeqCount
        
        ret =  dp[len(text1)-1][len(text2)-1]
        self.printDP(dp)
        print(ret)
        return ret

    def printDP(self, dp):
        for i in dp:
            print(i)

if __name__ == "__main__":
    sol = Solution()
    sol.longestCommonSubsequence("crabt", "cat")
    
    sol.longestCommonSubsequence("abcd", "abcd")

    sol.longestCommonSubsequence("abcd", "efgh")

    sol.longestCommonSubsequence("bsbininm", "jmjkbkjkv")

    sol.longestCommonSubsequence("hofubmnylkra", "pqhgxgdofcvmr")# 5

    sol.longestCommonSubsequence("oxcpqrsvwf", "shmtulqrypy")