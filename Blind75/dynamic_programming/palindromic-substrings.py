# Took 20 minutes
# Sorta just banged it out, not too sure if the logic is super clear yet
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.ret = 0
        for i, e in enumerate(s):
            l, r = i, i

            if l >= 0 and r + 1 < len(s) and s[l] == s[r+1]:
                self.helper(s, l, r+1)
                # we dont do selt.ret +=1 because the  self.helper will actuially count this case (aa) but this will count baab
            self.helper(s, l, r)
            
        return self.ret
    
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]: 
            self.ret += 1
            l -= 1
            r += 1
        
if __name__ == '__main__':
    s = Solution()
    #print(s.countSubstrings("abc")) # 3
    print(s.countSubstrings("aaa")) # 6
    print(s.countSubstrings("babad")) # 7
    print(s.countSubstrings("cbbd")) # 5
