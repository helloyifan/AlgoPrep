from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        head = 0
        tail = len(numbers)-1
        
        while head < tail:
            headTailSum = numbers[head] + numbers[tail]
            if headTailSum > target:
                tail -= 1
            elif headTailSum < target:
                head += 1
            elif headTailSum == target: 
                return [head + 1, tail + 1] # The input is "1 indexed"
            
        return None #Should be impossible

s = Solution()

numbers = [2,7,11,15]
target = 9
r1 = s.twoSum(numbers, target)
print(r1)

