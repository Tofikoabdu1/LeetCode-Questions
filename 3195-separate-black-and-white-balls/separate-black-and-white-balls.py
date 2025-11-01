class Solution:
    def minimumSteps(self, s: str) -> int:
        l=list(s)
        left =0
        right =0
        count = 0
        res = 0
        while right < len(s):
            if s[right]=='1':
                count+=1
                right+=1
            else :
                res+=count
                right+=1
        return res
            