# Took 45 min to solve it

# Not sure if optimal way
# But basically building a 2D array
# Where the cur val, must be the max of the prev row or the prev col
# If the cur index is a match, add that to cur val

# However, you do not want to count hits on the same letter twice for one word,
# should the prev rol / prev col must never be the cur row or cur col

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # text1 direction(v), text2 direction(>)
        dp = [[0]* len(text2) for i in range(len(text1))]
        
        
        for i1, t1 in enumerate(text1):
            for i2, t2 in enumerate(text2): # t2 being c of text2
                subSeqCount = 0 
                temp1 =0 
                temp2 =0

                if i1 > 0 and i2 > 0:
                    for dpVerticalIndex in range(0, i1): #not i1 +1 to avoid current col
                        temp1 = max(temp1, dp[dpVerticalIndex][i2-1])

                    for dpHorizontalIndex in range(0, i2): #not i2 +1 to avoid current row
                        temp2 = max(temp2, dp[i1-1][dpHorizontalIndex])


                #print(t1, t2, temp1, temp2)
                
                subSeqCount += max(temp1, temp2)
                         
                if t2 == t1:
                    subSeqCount += 1
                
                dp[i1][i2] = subSeqCount
        
        self.printDp(dp)
        ret = self.maxValIn2D(dp)
        print(ret)
        return ret
    
    def maxValIn2D(self, dp):
        maxV = 0
        for row in dp:
            for col in row:
                maxV = max(maxV, col)
        return maxV
        
    def printDp(self, dp):
        for i in dp:
            print(i)
    
if __name__ == "__main__":
    sol = Solution()
    # sol.longestCommonSubsequence("crabt", "cat")
    
    # sol.longestCommonSubsequence("abcd", "abcd")

    # sol.longestCommonSubsequence("abcd", "efgh")

    sol.longestCommonSubsequence("bsbininm", "jmjkbkjkv")

    # sol.longestCommonSubsequence("hofubmnylkra", "pqhgxgdofcvmr")# 5
