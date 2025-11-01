class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        l=[0]*(len(s)+1)
        for i in shifts:
            if i[2]==0:
                l[i[0]]-=1
                l[i[1] + 1] +=1
            else:
                l[i[0]]+=1
                l[i[1] + 1] -=1
        pref=[l[0]]
        for i in range(1,len(s)):
            pref.append(pref[-1]+l[i])
        # print(pref)
        res=[]
        for i in range(len(s)):
            newc =( ord(s[i]) - ord('a') + pref[i] ) % 26 + ord('a')
            res.append(chr(newc))
        return (''.join(res))

