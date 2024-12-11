# TC: O(n) We interate through one vector but look a constant time look up in otherhashmap
# SC: O(n) In the worst case there are no 0 and we store everything in hashmap 
class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.hm = {}
        for i, n in enumerate(nums):
            if n != 0:
                self.hm[i] = n
            

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ret = 0
        for i, n in enumerate(vec.nums):
            if n != 0 and i in self.hm:
                ret += n * self.hm[i]
        
        return ret

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)