class Solution:
    memo = [-1]*31
    def fib(self, n: int) -> int:
        def sol(n):
            memo = [-1]*31
            if n == 0 or n == 1:
                return n
            first = -1
            second = -1
            if memo[n-1] != -1: return memo[n-1]
            else: first = sol(n-1)
            if memo[n-2]!= -1: return momo[n-2]
            else: second = sol(n-2)
            memo[n]= first+second
            return memo[n]
        return sol(n)
    