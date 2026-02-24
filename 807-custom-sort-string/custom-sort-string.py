class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d= {}
        for idx , val in enumerate(order):
            d[idx] = val
        d2 = defaultdict(int)
        for c in s:
            d2[c]+=1
        # print(d ,d2)
        res = ''
        for c in d.values():
            if c in d2:
                res+=(d2[c]*c)
        for c in s:
            if c not in set(res):
                res+=d2[c]*c
        return res



        