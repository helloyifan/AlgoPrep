# Took 30 min to do both, but it was fun
class Solution:
    def topDown_uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1

        r1 = 0
        r2 = 0
        if m > 1:
            r1 = self.topDown_uniquePaths(m-1, n)
        
        if n > 1:
            r2 = self.topDown_uniquePaths(m, n-1)
        
        return r1 + r2
    
    def uniquePaths(self, m, n): #Bottom up, build 0,0 to m,n case
        dp = [[0 for _ in range(n)] for _ in range(m)] #2d [m][n]
        for mi in range(0, m):
            for ni in range(0, n):
                mIndexVal = 1 #cond if mi == 0 or ni ==0
                if mi > 0 and ni > 0:
                    mIndexVal = dp[mi-1][ni] + dp[mi][ni-1]
                
                dp[mi][ni] = mIndexVal

        return dp[m-1][n-1]

if __name__ == "__main__":
    sol = Solution()
    # print(sol.topDown_uniquePaths(3,3))
    print(sol.uniquePaths(3,3))
    print(sol.uniquePaths(3,6))


