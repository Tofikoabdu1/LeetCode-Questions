class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        res = []
        for i in responses:
            s =set(i)
            res.extend(list(s))
        # print(res)
        c = Counter(res)
        # print(c)
        maxf = max(c.values())
        ans = []
        for i in c:
            if c[i] == maxf:
                ans.append(i)
        return min(ans)


        