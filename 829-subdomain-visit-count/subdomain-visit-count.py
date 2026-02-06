class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        c = defaultdict(int)
        for domain in cpdomains:
            rep , d = domain.split()
            d = d.split(".")
            d.reverse()
            do = []
            for i in d:
                if not do:
                    do.append(i)
                else:
                    do.append(f"{i}.{do[-1]}")
                # c[i]+=int(rep)
            for i in do:
                c[i]+=int(rep)
        # print(c)
        res = []
        for k , v in c.items():
            res.append(f"{v} {k}")
        return res
        