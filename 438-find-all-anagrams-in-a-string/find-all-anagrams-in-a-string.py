class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        target  = Counter(p)
        window = Counter(s[:len(p)])
        res = []
        if target == window:
            res.append(0)
        for i in range(len(p) ,len(s)):
            if s[i] in window:
                window[s[i]]+=1
            else:
                window[s[i]] = 1
            window[s[i-len(p)]]-=1
            if window[s[i-len(p)]] == 0:
                del window[s[i-len(p)]]
            if window == target:
                res.append(i-len(p)+1)
        return res


        