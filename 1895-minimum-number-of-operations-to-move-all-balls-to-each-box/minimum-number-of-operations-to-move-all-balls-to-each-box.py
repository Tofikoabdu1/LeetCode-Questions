class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = []
        for i in range(len(boxes)):
            x =0
            for j in range( len(boxes)):
                if boxes[j]=='1':
                    x+=abs(j-i)
            res.append(x)
        return res
                    