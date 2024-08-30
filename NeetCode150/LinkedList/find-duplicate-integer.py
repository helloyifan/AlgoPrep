# 30 mins to revist a classic
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # Tortoise and hare algo
        # With tortoise and hare, you detect stay of the cycle
        slow, fast = 0, 0
        slow = nums[slow]
        fast = nums[fast]
        fast = nums[fast]

        # Since we know this linkedlist has a cycle
        # we use turotise and hare algo to determine where the 
        # intersection of the pointer 
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
        
        print("Interesction point cycle: ", slow)

        # however or this prbolem we are not necessarily looking for point of intersectiojn
        # we are looking for start of the cycle
        slow2 = 0
        while slow2 != slow:
            slow = nums[slow]
            slow2 = nums[slow2]
        
        # This is the turotise and hare algorithm
        # the combination of Cycle Detection and Finding the Start of the Cycle 
        # together is commonly referred to as the Tortoise and Hare algorithm 
        # (or Floyd's Cycle Detection algorithm). 
        print("Start of cycle: ", slow)

        return slow