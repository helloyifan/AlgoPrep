

# Find K-th Smallest Pair Distance

# This is actually a very difficult problem, i dont fully understand it still

# Given any distance, aim to count the number of pairs between that distance
# https://www.youtube.com/watch?v=bQ-QcFKwsZc&ab_channel=NeetCodeIO

# binary search soltuion is prefereed 

# Intuition
# Search space: 0, maxElementInInput
# L = 0 , R = max

# We know that thee search space represent the difference
# and the kth smallest is in there

# After sorting
# **We want to find the element, such that, it is the kth smallest, in the array**
# Helper function: 
#   count how many pairs that have the difference that less than or equal to k

from typing import List
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()

        # Do binary search on diff in values of array
        l = 0
        r = nums[len(nums)-1] - nums[0]
        
        # Binary search on diff in vals
        while l < r:
            med = (l + r)//2 # are these values always in the array?

            numOfPairs = self.countPairsInBetween(nums, med)
            if numOfPairs < k:
                l = med +1
            elif numOfPairs > k:
                r = med # The reason fro why its not med -1 is very specific too, i dont fully understand it, but we might skip the answer
            else:
                r = med
        return l 

    # Sliding window: Count number of pairs with distance <= maxDistance
    # This Helper function will Count how many pairs that have the difference that less than or equal to k
    def countPairsInBetween(self, nums, maxDistance):
        r, l = 0, 0
        count = 0
        while r < len(nums):
            while (nums[r] - nums[l]) > maxDistance:
                l += 1
            count += (r - l)
            r += 1
        print(count)
        return count


    # Another viable solution is with bucket sort
    # all the differences fit in a bucket
    # TC: O(n^2) to generate all the diffs (all the pairs essentially)
    # Use the bucket to tally it up
    # [1,3,1]
    # pairs: [1,3], [1,1], [3,1]
    # index       0, 1, 2, 3
    # bucketsort [1, 0, 2, 0]


    
    # Most brute force way fails because Memory Limit Exceeded
    # TC: O(n^2) to generate all the pair,s O(nlogn) to sort it 
    # SC O(n^2)
    def brute_forceSmallestDistancePair(self, nums: List[int], k: int) -> int:
        allPossiblePairs = []
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                allPossiblePairs.append((nums[i],nums[j]))
        #print(allPossiblePairs)
        data = []

        for pair in allPossiblePairs:
            data.append(abs(pair[0] - pair[1]))
        
        data.sort()
        print(data)
        print(data[k-1])
        
        return data[k-1]

sol = Solution()
sol.smallestDistancePair([1,3,1], 1)