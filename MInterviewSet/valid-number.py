class Solution:
    def isNumber(self, s: str) -> bool:
        # 1. Valid symbols
        if not self.isValidSymobls(s):
            return False

        # 1.5 Split it up 
        q = []
        curNumber = ''
        for c in s:
            if c.isnumeric():
                curNumber += c
            else:
                if curNumber != "":
                    q.append(curNumber)
                curNumber = ''
                q.append(c)

        if curNumber != '':
            q.append(curNumber)

        print(q)

        # 2. Decimal check 
        # Decimal invalid .. case
        
        oneDecFound = False
        for i, c in enumerate(q):
            if c == '.':

                if (i-1 < 0 or not q[i-1].isnumeric()) and (i+1 > len(q)-1 or not q[i+1].isnumeric()):
                    return False

                if oneDecFound:
                    print('double dec failure')
                    return False
                oneDecFound = True

        # 3. is Exponent chec


        return True

    def isValidSymobls(self, s):
        for c in s:
            if not c.isnumeric():
                if c != 'e' and c != 'E' and c != '+' and c != '-' and c != '.':
                    return False
        return True

sol = Solution()
#sol.isNumber('53.5e93')

print(sol.isNumber('.'))
print(sol.isNumber('1.'))
print(sol.isNumber('.1'))