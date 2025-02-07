# I totally got this incorrect
# TC: But its O(4^n), 
    # At each step we have up to 3 choices (+, -, *) and the ability to concatenate digits.
    # The worst case is when every digit is treated separately, leading to around 4 choices per digit.
    # There are n digits, so the number of recursive calls is about O(4^n).


# SC: We will go O(n) levels deep during DFS, and we will build finret based on the worst case of O(n) answers
# However we can also have O(4^n answers) so its O(n+4^n)

from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        
        def dfs(num, total, prevNum, path, finRet):

            if num == '':
                if total == target:
                    finRet.append(path)
                    return
                else:
                    return

            for i in range(1, len(num)+1):
                # Guard numbers like '05'. We allow for 0, but not numbers that start with a 0 and have numbers after it
                if len(num[:i]) > 1 and num[:i][0] == '0':
                    continue
                currentNum = int(num[:i])
                remainingNum = num[i:]

                # We need to handle the first number without operators
                if prevNum == None:
                    firstNumberPath = str(currentNum)
                    dfs(remainingNum, currentNum, currentNum, firstNumberPath, finRet)
                
                else:

                    addTotal = total + currentNum
                    multTotal = total - prevNum + (prevNum * currentNum)
                    subTotal = total - currentNum

                    addPath = path + '+' + str(currentNum)
                    updateAddPrevNum = currentNum # number that will be relevent to next operation
                    dfs(remainingNum, addTotal, updateAddPrevNum, addPath, finRet)

                    multPath = path + '*' + str(currentNum)
                    updatedMultPrevNum = prevNum * currentNum
                    dfs(remainingNum, multTotal, updatedMultPrevNum, multPath, finRet)

                    subPath = path +  '-' + str(currentNum)
                    updateSubPrevNum = -1* currentNum
                    dfs(remainingNum, subTotal, updateSubPrevNum, subPath, finRet)


            return
        
        finRet = []
        dfs(num, 0, None, '', finRet)
        return finRet


sol = Solution()
print(sol.addOperators("123", 6)) # ['1+2+3', '1*2*3']
print(sol.addOperators("232", 8)) # ['2+3*2', '2*3+2']
print(sol.addOperators("3456237490", 9191)) # [] 

print(sol.addOperators("105", 5)) # ['1*0+5', '10-5']
