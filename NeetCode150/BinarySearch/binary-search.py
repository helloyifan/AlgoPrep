from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        f, b = 0, len(nums)-1
        while f <= b:
            mid = (f + b)//2
            if  nums[mid] == target:
                return mid
            elif nums[mid] < target:
                f = mid + 1
            else:
                b = mid - 1
        return -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.search([-1,0,3,5,9,12], 9))
    print(sol.search([-1,0,3,5,9,12], 2))
    print(sol.search([-1,0,3,5,9,12], -1))
    print(sol.search([-1,0,3,5,9,12], 12))
    