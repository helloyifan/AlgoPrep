# Notes 5#Hello5#World
# Encode
# TC: O(n), we intentionally build strings by appending to a list and joining
# SC: O(n) for encoded List
# Decode 
# TC: O(n), we intentionally build strings by appending to a list and joining
# SC: O(n) for encoded List
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encodedList = []
        for s in strs:
            encodedList.append(str(len(s)))
            encodedList.append('#')
            encodedList.append(s)
        ret = ''.join(encodedList)
        print(ret)
        return ret
    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        ret = []
        index = 0
        while index < len(s):

            # Get number
            curNum = []
            while s[index] in '0123456789':
                curNum.append(s[index]) # O(1)
                index += 1
            curNum = ''.join(curNum)
            curNum = int(curNum)
            
            if s[index] == '#':
                index += 1
            
            ret.append(s[index:index+curNum])
            index += curNum
        
        return ret



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))