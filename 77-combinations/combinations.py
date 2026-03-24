class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        num = [i for i in range(1, n + 1)]
        res = []
        cur = []
        def backtrack(index):
            if len(cur) == k:
                res.append(cur[:])
                return
            for i in range(index, n):
                cur.append(num[i])
                backtrack(i + 1)
                cur.pop()
        backtrack(0)
        return res