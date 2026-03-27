class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        x = [0] * (n + 1)
        
        for s, e in requests:
            x[s] += 1
            x[e + 1] -= 1
            
        for i in range(1, n):
            x[i] += x[i-1]
        x.pop()
        x.sort()
        nums.sort()
        y = 0
        z = 10**9 + 7
        for i in range(n):
            y = (y + nums[i] * x[i]) % z
            
        return y