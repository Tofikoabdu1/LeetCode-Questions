class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        x = list(c.items())
        # print(x)
        y = sorted(x , key=lambda k: k[1])
        y.reverse()
        ans = ""
        for i in y:
            ans+=(i[0]*i[1])
        return ans



        