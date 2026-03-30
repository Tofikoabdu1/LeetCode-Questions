class Solution:
    def countGoodNumbers(self, n: int) -> int:
        m = 10**9 + 7
        
        def p(b, e):
            if e == 0: return 1
            res = p(b, e // 2)
            res = (res * res) % m
            if e % 2 == 1:
                res = (res * b) % m
            return res
        
        evens = (n + 1) // 2
        odds = n // 2
        
        return (p(5, evens) * p(4, odds)) % m