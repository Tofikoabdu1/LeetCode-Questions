class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res=10000000
        left = 0
        s = 0
        for right in range(len(nums)):
            s+=nums[right]
            while s >= target:
                res=min(res , right -left+1)
                s-=nums[left]
                left+=1
        if res==10000000:
            return 0
        return res
        