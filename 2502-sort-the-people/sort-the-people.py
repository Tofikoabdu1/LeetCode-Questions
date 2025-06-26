class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d={}
        for i in range(len(names)):
            d[heights[i]]=names[i]
        k=list(d.keys())
        k.sort()
        k.reverse()
        res=[]
        for n in k:
            res.append(d[n])
        return res