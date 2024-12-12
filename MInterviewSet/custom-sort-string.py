# TC: O(n) Over all this questions grows with the size of the s input
# every s input will require an operation so its O(n) where n = len(s)
# SC: O(n) Hashmap in the worst case can take O(n) where n = len(s) space
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dd = defaultdict(int) # count of all characters we have in input S
        # key is unique character
        # val is number of occurance
        for c in s:
            dd[c] +=1

        ret = ""
        # build the result
        # where we have the orders character first in order
        for i, e in enumerate(order):
            # if the character in the ordered list is in our dict
            if e in dd:
                # For each count of k, we add k to ret
                for _ in range(dd[e]):
                    ret += e
                # make sure to clean up from dict
                del dd[e]

        # take remaining unused key from our dict build from input S
        for k in dd:
            # add them to the outputaswell
            for _ in range(dd[k]):
                ret += k

        return ret