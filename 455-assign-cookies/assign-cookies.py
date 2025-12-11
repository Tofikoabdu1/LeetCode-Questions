class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        l = 0
        r =0
        count =0
        while l<len(s) and r<len(g):
            if s[l]>= g[r]:
                count+=1
                r+=1
            l+=1
        return count
