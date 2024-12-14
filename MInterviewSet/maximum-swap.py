# Note:
# 4 3 2 1 - Input 
# 4 3 2 1 - build a list of max from right to left (<--) 

# From fom left to right Take first swap that bigger
# You have to look at n+1 however for the max array you built

# 1 2 3 4 - Input
# 4 4 4 4

# 2 7 3 6 - Input
# 7 7 6 6 
# we take 7 from second index

# we also want to take last occurance of it 
# (as we want the biggest number)
# (meaning we need to keep traf of index)

# TC: O(n) We do two passes
# pass one to build rightToLeftMax 
# pass two to compare rightToLeftMax and numString List

# SC: O(n) for the rightToLeftMax we build

class Solution:
    def maximumSwap(self, num: int) -> int:
        # converting to string to make it easier to swap
        # joining the characters of the string and convert to int at end
        numStringList = [ch for ch in str(num)]

        rightToLeftMax = [None for _ in range(len(numStringList))]
        
        maxV = float('-inf')
        maxIndex = None
        for i in range(len(numStringList) -1, -1, -1):
            if int(numStringList[i]) > maxV:
                maxV = int(numStringList[i])
                maxIndex = i
            rightToLeftMax[i] = (maxV, maxIndex)

        swapFrom = None
        swapTo = None
        for i in range(len(numStringList)-1): #since we are looking at i+1
            if int(numStringList[i]) < rightToLeftMax[i+1][0]:
                swapFrom = i
                swapTo = rightToLeftMax[i][1]
                break

        retInt = num #If we dont want to swap
        if swapFrom != None and swapTo != None:
            temp = numStringList[swapTo]
            numStringList[swapTo] = numStringList[swapFrom]
            numStringList[swapFrom] = temp

            retInt = int("".join(numStringList))

        print(retInt)
        return retInt
