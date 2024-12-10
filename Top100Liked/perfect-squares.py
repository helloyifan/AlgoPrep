class Solution:
    def numSquares(self, n: int) -> int:

        perfectSquare = []
        curMax, counter = 0, 1
        while curMax < 10000:
            curPerfectSquare = counter*counter
            curMax = curPerfectSquare
            perfectSquare.append(curPerfectSquare)
            counter+=1


        q = []
        q.append(n)
        retNumbersThatHaveBeenAdded = 0
        while len(q)>0:
            repacementQ = []
            retNumbersThatHaveBeenAdded += 1
            while len(q)>0:
                cur = q.pop() 
                i = 0
                while perfectSquare[i] <= cur:
                    result = cur - perfectSquare[i]
                    if result == 0:
                        return retNumbersThatHaveBeenAdded
                    repacementQ.append(result)
                    i+=1
            q = repacementQ
        return
    
sol = Solution()
print(sol.numSquares(12))
print(sol.numSquares(13))