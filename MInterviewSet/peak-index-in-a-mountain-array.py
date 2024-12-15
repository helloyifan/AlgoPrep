# TC: Binary serach O(n)
# SC: O(1) we dont use additional memory except for two poitners
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr)-1
        
        while l <= r:
            m = (l+r)//2
            
            cond1 = False
            if m == 0 or arr[m-1] < arr[m]:
                cond1 = True

            cond2 = False
            if m == len(arr)-1 or arr[m+1] < arr[m]:
                cond2 = True
            
            if cond1 and cond2:
                return m
            
            if cond2 == False:
                l = m + 1
            else:
                r = m - 1
        return -1
x 