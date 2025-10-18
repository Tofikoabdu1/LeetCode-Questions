class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        x=nums[0]
        for i in range(len(nums)):
            if x!=0:
                return 0
            if nums[i]==x+i:
                continue
            else: return x+i
        return nums[-1]+1
