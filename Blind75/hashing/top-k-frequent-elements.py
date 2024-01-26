# took 15 mins


# It'd be good to learn how to sort a dict and get better at lambda functions
# Custom sorting function key= parm
# Custom lambda: lambda x: {use x somehow}

from collections import defaultdict

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        cache = defaultdict(int)
        for num in nums:
            cache[num] += 1
        
        # Sort the keys
        sorted_keys = sorted(cache, key=lambda x: cache[x] * -1) #*-1 for descending order
        counter = 0
        ret = []
        for key in sorted_keys:
            ret.append(key)
            counter += 1
            if counter == k:
                return ret
            
        return []



if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent([1,1,1,2,2,4], 2))
    print(s.topKFrequent([1], 1))