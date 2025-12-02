class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        n=len(nums)
        res = []
        for k in range(n-1):
            for i in range(n-1):
                temp=(nums[i]+nums[i+1])%10
                res.append(temp)
            # print(res)
            nums=res
            res=[]
            n-=1
        return nums[0]
        

        