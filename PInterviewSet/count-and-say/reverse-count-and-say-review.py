# Question: 
# Given an input string which is the output of a count and say method, return the original number.
# For example: If the number if "21", then the count and say method would return
# "1211" (one two, one one). In this problem, the input provided to us is "1211" and our goal is to return "21".

# defaultdict(<class 'list'>, {'11': [['1']], '1211': [['2', '1'], ['1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111']], '1': []})
# ['21', '1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111']

# Notes: 
# The trick is to derive that '11': [['1']] and use that to buld '1211': [ ['2', '1'], ....]

# TC: 
# * O(2^n) because at each level we have n binary decision process at each character (split or not).
# * The function explores all possible partitions of the input string.
# * At each step, it decides where to split, leading to a binary branching pattern.

# SC: 
# * Recursive call stack: In the worst case, the depth of recursion is O(n), but the total number of function calls stored is still O(2ⁿ).
# * Memoization (dd dictionary): Stores results for all possible substrings, which can be up to O(2ⁿ) in size.


from collections import defaultdict
class Solution:
    def reverseCountAndSay(self, input):
        ret = []
        dd = defaultdict(list)
        def dfs(input):
            if len(input) == 0:
                return [[]]

            # we already have the result for count and say here so its redundant to do it again
            if input in dd:
                return dd[input]

            # Build from front to back
            for i in range(1, len(input)):
                count = int(input[:i])
                digitString = input[i]

                # if i == len(input)-1
                # this is a bit weird, bcuz [i+1] is out of bound
                # this is a bit weird, but [i+1:] will result in ''
                remainingString = input[i+1:]

                remainingStringCountAndSay = dfs(remainingString)
                for t in remainingStringCountAndSay:
                    # Create current count and say 
                    # but it in dd for reuse by other levels
                    # the structures is a list of entries like ['2','1'] (one two, one one)
                    curLevelCountAndSay = [digitString * int(count)]

                    # Join with results from remainingString
                    curLevelCountAndSay.extend(t)

                    dd[input].append(curLevelCountAndSay)

            return dd[input] # current input count and say
        
        # Post processing results
        dfs(input)
        listOfStringForFinalResult = []
        print(dd)
        for ret in dd[input]:
            listOfStringForFinalResult.append(''.join(ret))
        
        print(listOfStringForFinalResult)
        return listOfStringForFinalResult

sol = Solution()
sol.reverseCountAndSay("1211") # 21, 111111