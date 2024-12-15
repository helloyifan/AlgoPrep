# Kth missing postiive integer
# Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.


# TC: O(len(arr) + k) size 
# SC: O(len(arr)) space
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        d = {}
        for i in arr:
            d[i] = True
        
        countOfMissing = 0
        counter=1
        while countOfMissing < k:
            if not counter in d:
                countOfMissing +=1
            counter +=1
        return counter -1 # We over count by 1 (-1 to accomodate)    
            
