# Did it on neetcode and it took 26mins, debugged alot of edge cases

# Complexity Analysis
# Time Complexity: O(n) for loop
# Space Complexity: O(n) potetnially everything can be on the stack

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 0:
            return 0
        stack = []
        for t in tokens:
            if not self.isArith(t):
                stack.append(int(t))
            else:
                v2 = stack.pop()
                v1 = stack.pop()
                valAfterArithmetic = self.performArith(v1, v2, t)
                print(valAfterArithmetic)
                stack.append(valAfterArithmetic)
        return stack[0]
    
    def isArith(self, character):
        if character in ["+", "-", "*", "/"]:
            return True
        return False
    
    def performArith(self, v1 , v2, sign):
        print(v1, v2, sign)
        if sign == "+":
            return (v1 + v2)
        elif sign == "-":
            return (v1 - v2)
        elif sign == "*":
            return (v1 * v2)
        elif sign == "/":
            return int(v1 / v2) #this rounding is very specific, cant be math.floor because -0.4 rounds to -1
        else:
            raise Exception("Error invalid arith sign")
        


if __name__ == "__main__":
    sol = Solution()
    # tokens = ["1","2","+","3","*","4","-"]
    # ret = sol.evalRPN(tokens)
    # print(ret)

    # tokens2 = ["19"]
    # ret2 = sol.evalRPN(tokens2)
    # print(ret2)

    #tokens3 = ["4","13","5","/","+"]
    #ret3 = sol.evalRPN(tokens3)
    #print(ret3)

    tokens4=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    ret4 = sol.evalRPN(tokens4)
    print(ret4)

    # 9+3 = 12
    # 12*-11 = -132
    # 6/132 = 0
    # 10 * 0 = 0
    # 0 + 17 = 17
    # 17 + 5 = 22