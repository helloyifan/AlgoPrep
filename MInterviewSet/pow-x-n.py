# Note: Optimal solution is to divide and concour (by halving n recursively)
# TC: O(logN)
# SC: O(logN) #depending on how many times we can half N
class Solution:
    def myPow(self, x: float, n: int) -> float:

        def helper(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x

            halfOfProduct = helper(x, n//2)

            remainderOfProduct = helper(x, n%2)

            totalProduct = halfOfProduct * halfOfProduct * remainderOfProduct
            return totalProduct

        negMode = False
        if n < 0:
            negMode = True
            n *= -1


        powVal = helper(x, n)
        if negMode:
            powVal = 1/powVal
        print(powVal)
        return powVal
    
# O(N) answer
    def naiveLinearSolution(self, x: float, n: int) -> float:
        
        negMode = False
        if n < 0:
            negMode = True
            n *=-1

        powVal = 1
        for i in range(n):
            powVal *= x
        
        if negMode == True:
            powVal = 1/powVal
        
        print(powVal)
        return powVal
    
sol = Solution()
sol.myPow(2.0000, 10)
sol.myPow(2.0000, -2)
sol.myPow(2.0000, 0)
sol.myPow(0, 2)
sol.myPow(1, -2)
