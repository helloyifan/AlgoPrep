# Notes: The interesting case is ")(", the key here is that if there are 0 openings
# Then keep track of the unopenedClosed
# TC: O(n) one pass
# SC: O(1)
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        unClosedOpenings = 0
        unopenedClosed =0 

        for i, e in enumerate(s):
            if e == "(":
                unClosedOpenings += 1
            if e == ')':
                if unClosedOpenings == 0:
                    unopenedClosed +=1
                else:
                    unClosedOpenings -= 1
        
        return unClosedOpenings + unopenedClosed
