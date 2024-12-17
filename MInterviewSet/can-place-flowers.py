# TC: O(n) we check through every element of flowerbed
# SC: O(1), we dont use additional space
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        validSpots = 0
        for i, e in enumerate(flowerbed):
            # Cur is 0, next end or 0, prev is start or 0
            if flowerbed[i] == 0 and (i+1 == len(flowerbed) or flowerbed[i+1] == 0) and (i == 0 or flowerbed[i-1] == 0):
                flowerbed[i] = 1 #remove valid spot for future
                validSpots +=1
        
        return validSpots >= n
