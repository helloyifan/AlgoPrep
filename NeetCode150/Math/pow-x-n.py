# Solved in 25min, both O(n) and O(log(n))
# Divide and  concour, once we solved half of it, we can muplity it to itself
class Solution:
    # naive solution (O(n))
    def linearTimeSolution(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        isNeg = False
        if n < 0:
            isNeg = True
        
        ret = x
        
        for _ in range(abs(n) - 1):
            ret = ret * x

        if isNeg:
            ret = 1/ret

        print(ret)
        return ret
    
    # O(log(n)) solution
    # calculate power to apply
    # better solution is to divide and concor
    # what that means is take, if we divide n by 2
    # and we muplitied the result of it n divied by 2 by 2. then thats log(n)
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):            
            if n == 0:
                return 1
            prevRet = helper(x, n//2)
            remainder = n%2

            curRet = 1 # start off at 1
            if remainder > 0:
                curRet = curRet * x

            curRet = curRet * prevRet * prevRet            
            return  curRet
     
        
        isNeg = False
        if n < 0:
            isNeg = True
            n = abs(n)

        alwayPosRet = helper(x, n)
        finRet = alwayPosRet
        if isNeg:
            finRet = 1/alwayPosRet

        #print(finRet)
        return finRet

sol = Solution()
sol.myPow(2.00000, 5) # 32.00000
sol.myPow(1.10000, 10) # 2.59374
sol.myPow(2.00000, -3) # 0.12500
 
