# watched youtube video for the 4#neet4#cide4#love1#you idea
# jittery coffee implementation took like 20 mins
from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for s in strs:
            count = len(s)
            ret += str(count) +"#"  + s
        return ret

    def decode(self, s: str) -> List[str]:
        ret = []
        remainingS = s
        while len(remainingS) > 0:
            hashLoc = remainingS.find("#")

            # wordLen
            wordLen = int(remainingS[:hashLoc])
            wordStart = hashLoc +1 
            wordEnd = wordStart + wordLen
            curWord = remainingS[wordStart:wordEnd]
            remainingS = remainingS[wordEnd:]
            ret.append(curWord)
        
        return ret

if __name__ == "__main__":
    sol = Solution()
    encode = sol.encode(["neet","cide","love","you"])
    decode = sol.decode(encode)
    print(encode)
    print(decode)

    encode1 = sol.encode(["neetneetneetneet","codecodecodecodecodecode","lovelovelove","youyouyouyouyouyou"])
    decode1 = sol.decode(encode1)
    print(encode1)
    print(decode1)
