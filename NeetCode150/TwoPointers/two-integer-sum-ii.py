from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        f = 0
        b = len(numbers) - 1
        
        while f < b:
            curVal = numbers[f] + numbers[b]
            print(curVal)
            if curVal == target:
                return [f + 1, b + 1]
            elif curVal < target:
                f += 1
            elif curVal > target: 
                b -= 1

        return None

if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum([1,2,3,4], 3))



    #2,5,6,8,9

