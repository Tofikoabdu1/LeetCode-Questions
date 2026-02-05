class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        cont=set()
        for x,y in ranges:
            for i in range(x,y+1):
                cont.add(i)
        for i in range(left,right+1):
            if i not in cont:
                return False
        return True
        