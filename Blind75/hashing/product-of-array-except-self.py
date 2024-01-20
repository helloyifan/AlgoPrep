class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        prefix = 1 
        prefixList = [] # Build a list of prefix withing current number
        for num in nums:
            prefixList.append(prefix) # We do that by incrementing until after appending
            prefix *= num

        suffix = 1
        suffixList = []
        for num in reversed(nums): # Do the same from back to front
            suffixList.append(suffix)
            suffix *= num
        suffixList = suffixList[::-1] #Flip the array so it matches up with prefix for same index i


        ret = []
        for i, e in enumerate(nums):
            ret.append(prefixList[i] * suffixList[i])

        return ret