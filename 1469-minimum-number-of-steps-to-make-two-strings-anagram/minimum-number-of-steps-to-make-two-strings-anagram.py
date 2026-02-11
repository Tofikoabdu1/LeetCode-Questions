class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c1 = Counter(s)
        c2 = Counter(t)
        # print(c1)
        # print(c2)
        cnt = 0
        for i in c1:
            if i in c2:
                if c1[i] > c2[i]:
                    cnt+=(c1[i]-c2[i])
            else:
                cnt+=c1[i]
        return cnt

        