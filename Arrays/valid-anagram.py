from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i, val in enumerate(s):