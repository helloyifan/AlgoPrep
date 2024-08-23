# Solved in around 30 mins
# kind of tired when i solved this one but not that complicated
# Just iterateively move two pointers to mimic the right actions
from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        f, b = 0, 0

        hashSet = defaultdict(int)
        for c in s1:
            hashSet[c] += 1

        
        while b < len(s2): #Keep doing this until the back hits the end
            # While we move the b ptr, we remove from hashset

            print(f, b)
            while b < len(s2):
                if(self.checkIfWeCanStopPos(hashSet)):
                    break
                curChar = s2[b]
                hashSet[curChar] -= 1
                b += 1

            if (self.checkIfWeCanStop(hashSet)):
                return True

            # While we move the f ptr, we add to hashset

            while f < b:
                if (self.checkIfWeCanStopNeg(hashSet)):
                    break
                curChar = s2[f]
                hashSet[curChar] += 1
                f +=1
            
            if (self.checkIfWeCanStop(hashSet)):
                return True

        return False
    

    def checkIfWeCanStop(self, l):
        print(l)
        for i, e in enumerate(l):
            if l[e] != 0:
                return False
        return True

    def checkIfWeCanStopPos(self, l):
        for i, e in enumerate(l):
            if l[e] > 0:
                return False
        return True
    
    def checkIfWeCanStopNeg(self, l):
        for i, e in enumerate(l):
            if l[e] < 0:
                return False
        print("yup")
        return True
if __name__  == '__main__': 
    sol = Solution()
    # print(sol.checkInclusion( "ab", "eidbaooo"))
    # print(sol.checkInclusion( "ab", "lecabee"))

    # print(sol.checkInclusion( "ab", "eidboaoo"))
    print(sol.checkInclusion( "hello", "ooolleoooleh"))
