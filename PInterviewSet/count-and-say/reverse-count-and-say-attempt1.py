# Question: 
# Given an input string which is the output of a count and say method, return the original number.
# For example: If the number if "21", then the count and say method would return
# "1211" (one two, one one). In this problem, the input provided to us is "1211" and our goal is to return "21".


from collections import defaultdict
class Solution:
    def sample_reverseCountAndSay(self, s):
        dic = defaultdict(list)

        def recursive(s):
            if not s:
                return [[]]
            if s in dic:
                return dic[s]
            for i in range(1, len(s)):
                count, num = int(s[:i]), s[i]
                for subres in recursive(s[i+1:]):
                    dic[s].append([count * num] + subres)
            return dic[s]
        
        recursive(s)
        ret = [''.join(subres) for subres in dic[s]]
        print(dic)
        return ret
    
    # Top down recursion
    def reverseCountAndSay(self, s):
        dd = defaultdict(list)

        def recursion(s):
            if s == '':
                return [[]]
            
            # Memoized
            if s in dd:
                return dd[s]
            
            for i in range(1, len(s)): # 1 because the first letter cannot be a digit
                count = int(s[:i])
                digitString = s[i]

                temp = recursion(s[i+1:]) # Give me the rets for the rest of the string
                for t in temp: # For each ret of the rest of the string, add in the current level
                    particalRet = [digitString * count]
                    fullRet = particalRet + t #join the old ret with the new ret
                    dd[s].append(fullRet)
            return dd[s]

        recursion(s)
        # Post process result
        validResults = dd[s]
        finRet = []
        for r in validResults:
            finRet.append(''.join(r))
        return finRet

sol = Solution()
print(sol.sample_reverseCountAndSay('1211'))
#print(sol.reverseCountAndSay('1211'))
