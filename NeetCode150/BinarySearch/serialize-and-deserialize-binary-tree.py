from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        q=deque()
        q.append(root)
        ret = []

        while len(q) > 0:
            tempQ = deque()
            tempRet = []
            notNone = False
            while len(q) > 0:
                head = q.popleft()
    
                if head == None:
                    ret.append('None')
                    continue

                ret.append(str(head.val))
                #notNone = True
                tempQ.append(head.left)
                tempQ.append(head.right)

            q = tempQ
        
            #if notNone:
            #    ret.extend(tempRet)
        print(ret)
        return ','.join(ret)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        dataList= data.split(',')
        dataHeadIdx = 0 
        nodeQ = deque()
        firstNode = TreeNode(dataList[dataHeadIdx])
        dataHeadIdx += 1

        nodeQ.append(firstNode)

        while len(nodeQ) > 0:
            tempQ = deque()
            while len(nodeQ) > 0:
                head = nodeQ.popleft()

                if(dataHeadIdx == len(dataList)):
                    break

                leftNode = TreeNode(dataList[dataHeadIdx])
                dataHeadIdx+=1
                head.left = leftNode
                tempQ.append(leftNode)

                if(dataHeadIdx == len(dataList)):
                    break

                rightNode = TreeNode(dataList[dataHeadIdx])
                dataHeadIdx+=1


                head.right = rightNode
                tempQ.append(rightNode)
            nodeQ = tempQ

        return firstNode
    

sol = Codec()
head = TreeNode(
    val=1,
    left=TreeNode(val=2),
    right=TreeNode(
        val=3,
        left=TreeNode(val=4),
        right=TreeNode(val=5)
    )
)
print(sol.serialize(head))

#sol.deserialize([1,2,3,None,None,4,5])

## Test 2

print(sol.serialize(None))
