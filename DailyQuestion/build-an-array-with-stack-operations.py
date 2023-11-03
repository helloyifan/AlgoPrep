class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:        
        ret = []
        targetPointer = 0 
        
        for i in range(1, n+1):
            if (i == target[targetPointer]):        
                ret.append("Push")
                targetPointer += 1
            else:
                ret.append("Push")
                ret.append("Pop")

            if (targetPointer > len(target)-1):
                return ret
            
        return ret