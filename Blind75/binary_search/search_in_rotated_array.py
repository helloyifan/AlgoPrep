
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        t = target

        N = len(nums)
        s, e = 0, N - 1

        while s <= e:
            m = (s + e)//2

            if m == t:
                return m
            elif m > t:
                if t > nums[N-1]:
                    e = m + 1
                else:
                    s = m + 1
            elif m < t:
                if t > nums[N-1]:
                    s = m + 1
                else:
                    e = m + 1


if __name__ == '__main__':
    sol = Solution()
    print(sol.search( [4,5,6,7,0,1,2], 0))

    print(sol.search( [4,5,6,7,0,1,2], 8))

    print(sol.search( [1], 0))

    print(sol.search( [1], 1))