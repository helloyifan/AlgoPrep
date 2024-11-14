'''
I want a 9 digit number
contain all the digits 1 to 9 once

1st 1 numbers from the left are divisible by 1
1st 2 numbers from the left are divisilbe by 2

1st 9 numbers from the left are divisible by 9
....


'''

class Solution():
    def generate9DigitNum(self):
        
        def dfs(currentDigitCount, existingNumber, visited):
            currentDigitCount += 1
            if currentDigitCount == 10:
                return True, existingNumber

            for i in range(1, 10):
                currentNumberToAdd = 10 * existingNumber + i 
                if not i in visited:
                    if currentNumberToAdd % currentDigitCount == 0:
                        visited.add(i)
                        cond, ret = dfs(currentDigitCount, currentNumberToAdd, visited)
                        if cond == True:
                            return True, ret
                        visited.remove(i)

            return False, -1
        
        cond, ret = dfs(0, 0, set())
        return ret 

sol = Solution()
ret = sol.generate9DigitNum()
print(ret)


## Notes
# 1 1 
# 22 2
# 333 3
# 