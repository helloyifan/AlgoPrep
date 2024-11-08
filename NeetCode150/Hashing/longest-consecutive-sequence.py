from typing import List
from collections import defaultdict

# sortingNlogNSolution:
# Time Analysis: O(nlogn) for sort, n for loop, n for the other for loop O(nlog+n+n) = O(nlogn)
# Space Analysis: O(n) for dp

# hashSetlongestConsecutive
# Time Analysis: O(n) for outerloop, O(n) for innerloop, 
#   note that each element will be accessed at most twice, because we are checking for start
#   if an element is the start, it wont be checked in the inner loop
#   final time complexity = O(n)

# Space Analysis: O(n) for hashset

class Solution:
    def sortingNlogNSolution(self, nums: List[int]) -> int:
        dp = {}
        nums.sort()
        for n in nums:
            if not n+1 in dp:
                if not n in dp:
                    dp[n+1] = 1
                else:
                    prevLen = dp[n]
                    del dp[n]
                    dp[n+1] = prevLen+1

        maxRet = 0
        for k in dp:
            maxRet = max(maxRet, dp[k])
        print(dp)
        return maxRet
    
    def hashSetlongestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        maxLen = 0
        for n in nums:
            # if ur checking n=100, make sure that 99 isnt therem bcuz if it was 100 wouldnt be the start
            if not (n-1) in hashset: 
                cur = n
                curLen = 0
                # check 
                while cur in hashset:
                    curLen += 1
                    cur +=1 
                maxLen = max(maxLen, curLen)
        return maxLen



if __name__ == '__main__':
    sol = Solution()

    print(sol.longestConsecutive([2,20,4,10,3,4,5])) # 4
    #print(sol.longestConsecutive([0,3,2,5,4,6,1,1])) # 7

    # print(sol.longestConsecutive([100,4,200,1,3,2]))
    # print(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
    # print(sol.longestConsecutive([]))
    # print(sol.longestConsecutive([100, 100, 100, 100, 100, 99, 101]))