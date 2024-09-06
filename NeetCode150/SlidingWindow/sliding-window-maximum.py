from typing import List

# NaiveTimeOutSolutioon took 12 mins
# someOptimizationReducingFrequencyOfMax took 15mins
# tried again for 20 min
# Troed and succeded in 20mins, but kinda knew the solution already
class Solution:
    def naiveTimeOutSolution(self, nums: List[int], k: int) -> List[int]:
        f, b = 0, 0
        
        maxList = []
        maxStack = []
        for i in range(k):
            curV = nums[i]
            maxStack.append(curV)

        maxList.append(max(maxStack))
        for i in range(k, len(nums)):
            curV = nums[i]
            maxStack.pop(0)
            maxStack.append(curV)
            maxList.append(max(maxStack))

        print(maxList)
        return maxList
    
    def someOptimizationReducingFrequencyOfMax(self, nums: List[int], k: int) -> List[int]:
        maxList = []
        maxVal = float("-inf")

        for i in range(k):
            curV = nums[i]
            maxVal = max(maxVal, curV)

        maxList.append(maxVal)
        for i in range(k, len(nums)):
            curV = nums[i]
            numToRemove = nums[i - k]
            
            if numToRemove == maxVal:
                newStart = i - k + 1 # +1 to exlcude the cur Element
                newEnd = i
                if newStart < newEnd:
                    curSubset = nums[i - k + 1: i] 
                    maxVal = max(curSubset)
                else:
                    maxVal = float("-inf") #basically ignore until next line

            maxVal = max(maxVal, curV)
            maxList.append(maxVal)

        #print(maxList)
        return maxList


    def triedAgain(self, nums: List[int], k: int) -> List[int]:
        maxList = []
        maxStack = [] #what if instead of num, we stored index
        for i in range(k):
            curV = nums[i]
            
            if len(maxStack) > 0 and curV > maxStack[0]:
                maxStack = []
            
            maxStack.append(curV)
        maxList.append(max(maxStack))
        
        for i in range(k, len(nums)):
            curV = nums[i]

            if len(maxStack) == k:
                maxStack.pop(0)

            if len(maxStack) > 0 and curV > maxStack[0]:
                maxStack = []

            # You need to find the right place to add it 

            while len(maxStack) > 0 and maxStack[-1] < curV:
                print(maxStack)
                maxStack.pop()

            maxStack.append(curV)
            print("huh: ", maxStack)
            maxList.append(maxStack[0])

        print(maxList)
        return maxList
    
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxList = []
        maxIndexStack = [] #what if instead of num, we stored index

        for i, e in enumerate(nums):
            # Evict head if its more then k away
            if maxIndexStack and maxIndexStack[0] < i-k + 1: #1 to address the offset
                maxIndexStack.pop(0)

            # Evict back if cur number is
            while maxIndexStack and nums[i] > nums[maxIndexStack[-1]]:
                maxIndexStack.pop()

            # Always add the current index
            maxIndexStack.append(i)
            curLargestNumberInSubset = nums[maxIndexStack[0]]
            
            if i >= k - 1: # 1 to address the offset
                maxList.append(curLargestNumberInSubset)

        #print(maxList)
        return maxList


if __name__ == '__main__':
    sol = Solution()

    # nums = [1,3,-1,-3,5,3,6,7]
    # k = 3
    # sol.maxSlidingWindow(nums, k)

    # nums1 = [1]
    # k1 = 1
    # sol.maxSlidingWindow(nums1, k1)

    # nums2 = [1, -1]
    # k2 = 1
    # sol.maxSlidingWindow(nums2, k2)

    nums3 = [1,3,1,2,0,5]
    k3 = 3
    sol.maxSlidingWindow(nums3, k3) #[3,3,2,5]

