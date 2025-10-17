class Solution:
    def romanToInt(self, s: str) -> int:
        roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        res=0
        i=0
        while i < len(s):
            y=s[i]
            x = s[i:i+2]
            if x in roman:
                res+=roman[x]
                i+=2
            else:
                res+=roman[y]
                i+=1
        return res