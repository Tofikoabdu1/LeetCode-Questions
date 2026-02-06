class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        c = defaultdict(list)
        for p in paths:
            p = p.split()
            path = p[0]
            files = p[1:]
            # print(files)
            for f in files:
                name , content = f.split(".txt")
                p = path + "/" + name + ".txt"
                c[content].append(p)
            res = []
            for k , val in c.items():
                if len(val)>1:
                    res.append(val)
            # print(c)
        return res

            
        
