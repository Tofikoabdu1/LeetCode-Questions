class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        def backtrack(current):
            if len(current) == len(nums):
                res.append(current[:])
                return
            for n in nums:
                if n not in current:
                    current.append(n)
                    backtrack(current)
                    current.pop()
        
        backtrack([])
        return res