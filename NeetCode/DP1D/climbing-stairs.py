class Solution:
    # Fibonacci sequence
    def climbStairs(self, n: int) -> int:
        prevRet = 0
        ret = 0

        for i in range(n): # range goes from 0 to n-1
            if (i < 2): # Because for the first two steps its base case
                ret = 1

            temp = ret + prevRet
            prevRet = ret
            ret = temp

        return ret




# 1

# 1 1
# 2

# 1 1 1
# 2 1
# 1 2

# 1 1 1 1
# 2 1 1 
# 1 2 1 
# 1 1 2 
# 2 2 

# 1 1 1 1 1
# 2 1 1 1
# 1 2 1 1
# 1 1 2 1
# 1 1 1 2
# 2 2 1
# 2 1 2
# 1 2 2 


s  = Solution()
n2 = 2
r2 = s.climbStairs(n2)
print(r2)

n3 = 3
r3 = s.climbStairs(n3)
print(r3)

n4 = 4
r4 = s.climbStairs(n4)
print(r4)

n5 = 5
r5 = s.climbStairs(n5)
print(r5)