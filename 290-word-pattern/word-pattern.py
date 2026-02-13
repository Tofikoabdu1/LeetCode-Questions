class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p = list(pattern)
        s2 = list(map(str , s.split()))
        # print(p,s2)
        if len(p) != len(s2):
            return False
        d = defaultdict(str)
        used=set()
        for i in range(len(p)):
            if p[i] in d:
                if d[p[i]] != s2[i]:
                    return False
            else:
                if s2[i] in used:
                    return False
            used.add(s2[i])

            d[p[i]] = s2[i]
        return True



        