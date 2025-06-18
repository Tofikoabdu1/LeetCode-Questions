class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        x=0
        for i in range(len(nums)):
            if nums[i]==x:
                x+=1
            else: return x
        return x
