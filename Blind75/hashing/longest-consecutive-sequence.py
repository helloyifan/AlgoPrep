class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sequences = [] # {s: 1, e: 2}
        hash = {i : True for i in nums}
        for num in nums:
            hit = False
            for s in sequences:
                if num == s['s'] - 1:
                    s['s'] = num
                    # hash.pop(num)
                    hit = True
                elif num == s['e'] + 1:
                    s['e'] = num
                    # hash.pop(num)
                    hit = True

            if hit == False:
                sequences.append({'s': num, 'e': num})
        # TODO we have to join the sequenes togetehr
        maxLen = 0
        for s in sequences:
            maxLen = max(maxLen, s['e'] - s['s'])

        return maxLen


if __name__ == '__main__':
    sol = Solution()
    # print(sol.longestConsecutive([100,4,200,1,3,2]))

    print(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))

    #print(sol.longestConsecutive([]))

    # print(sol.longestConsecutive([100, 100, 100, 100, 100, 99, 101]))