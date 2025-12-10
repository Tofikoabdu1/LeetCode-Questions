class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        res = []
        for i in range(n):
            if len(nums)==1:
                return nums[0]
            for i in range(len(nums)-1):
                res.append((nums[i]+nums[i+1])%10)
            nums = res
            res = []
        return nums[0]



        