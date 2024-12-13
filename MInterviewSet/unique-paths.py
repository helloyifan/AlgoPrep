
# TC: O(mxn) for bottom up dp population
# SC: O(mxn) one index for each cell

def uniquePaths(m: int, n: int) -> int:
    dp = [[0 for _ in range(n) ] for _ in range(m)]

    # Declaring Basecase
    for i in range(n):
        dp[0][i] = 1
        
    for i in range(m):
        dp[i][0] = 1
    
    # 
    for i in range(m):
        for j in range(n):     
            if i-1 >= 0 and j-1 >= 0:
                dp[i][j] = dp[i-1][j] +  dp[i][j-1]
    return dp[m-1][n-1]
