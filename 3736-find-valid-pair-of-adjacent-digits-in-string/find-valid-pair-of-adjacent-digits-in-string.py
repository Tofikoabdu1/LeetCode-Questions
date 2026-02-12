class Solution:
    def findValidPair(self, s: str) -> str:
        c=Counter(s)
        # print(c)
        for i in range(len(s)-1):
            if s[i] != s[i+1]:
                x , y= int(s[i]) , int(s[i+1])
                if c[s[i]] == x and c[s[i+1]] == y:
                    return s[i:i+2]
        return ""