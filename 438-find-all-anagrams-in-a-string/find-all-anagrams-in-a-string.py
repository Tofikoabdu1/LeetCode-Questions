class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        p_count=Counter(p)
        count = Counter(s[:k])
        res = []
        for i in range(len(s)-k):
            if p_count == count:
                res.append(i)
            count[s[i]] -=1
            count[s[i+k]] +=1
        if count == p_count:
            res.append(len(s)-k)
        return res

        