class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        def back(s):
            if len(s)==n:
                res.append("".join(s))
                return
            if s[-1] == "a":
                s.append("b")
                back(s)
                s.pop()
                s.append("c")
                back(s)
                s.pop()
            elif s[-1] == "b":
                s.append("a")
                back(s)
                s.pop()
                s.append("c")
                back(s)
                s.pop()
            elif s[-1] == "c":
                s.append("a")
                back(s)
                s.pop()
                s.append("b")
                back(s)
                s.pop()
        back(["a"])
        back(["b"])
        back(["c"])
        print(res)
        print(len(res))
        if len(res)>=k:
            return res[k-1]
        else:
            return ""
            



        