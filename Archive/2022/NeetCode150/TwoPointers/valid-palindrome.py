class Solution:
    def isPalindrome(self, s: str) -> bool:
        if (len(s) == 1):
            return True
        s  = s.lower()
        
        head = 0
        tail = len(s) - 1

        while (head < tail):
            if (not s[head].isalnum()):
                head += 1
                continue
            
            elif(not s[tail].isalnum()):
                tail -= 1
                continue

            elif(s[head].lower() != s[tail].lower()):
                return False
        
            # only do this if we make it here
            head+=1
            tail-=1
        # If we didnt fail
        return True


sol = Solution()

s1 = "A man, a plan, a canal: Panama"
r1 = sol.isPalindrome(s1)
print(r1)

s2 = "race a car"
r2 = sol.isPalindrome(s2)
print(r2)

s3 = "  a  "
r3 = sol.isPalindrome(s3)
print(r3)

