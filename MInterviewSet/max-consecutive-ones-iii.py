# Note: Sliding window question, treat 0 like 1, but maintain a zeroCounter
# When zeroCounter gets too high, move up L pointer
# TC: O(n) - At most we process each num 2 times so it will be O(2n) which is O(n)
# SC: O(1)
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r = 0, 0

        maxOnes = 0
        curOnes = 0

        zeroCounter = 0
        while r < len(nums):
            if nums[r] == 1:
                curOnes += 1
            else: #nums[r] == 0:
                zeroCounter += 1
                curOnes += 1
                while zeroCounter > k:
                    if nums[l] == 0:
                        zeroCounter -= 1
                    curOnes -= 1
                    l+=1

            maxOnes = max(maxOnes, curOnes)
            r += 1

        return maxOnes 