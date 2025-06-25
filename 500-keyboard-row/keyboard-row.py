class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1 = "qwertyuiop"
        r2 = "asdfghjkl"
        r3 = "zxcvbnm"
        res=[]
        for w in words:
            w1=w.lower()
            if len(set(r1+w1))==len(r1):
                res.append(w)
            elif len(set(r2+w1))==len(r2):
                res.append(w)
            elif len(set(r3+w1))==len(r3):
                res.append(w)
        return res
        