class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = 0 
        j = 0
        res = []
        while i < len(firstList) and j < len(secondList):
            f1 , f2 =firstList[i]
            s1 , s2 = secondList[j]
            if f1 <= s2 and s1 <= f2:
                res.append([max(f1,s1),min(f2,s2)])
            if s2 <= f2:
                j+=1
            else:
                i+=1
        return res