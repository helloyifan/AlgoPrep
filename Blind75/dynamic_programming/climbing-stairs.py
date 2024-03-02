# Took 10 mins bcuz im stuiiopd
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """ 
        ret = 1
        prev = 0
        for i in range(0, n):
            temp = ret
            ret = ret + prev
            prev = temp

        return ret

if __name__ == '__main__':
    sol = Solution()
    print(sol.climbStairs(2))
    print(sol.climbStairs(3))
    print(sol.climbStairs(4))
    print(sol.climbStairs(45))