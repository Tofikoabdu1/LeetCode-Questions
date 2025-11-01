class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res=[nums[0]]
        for i in range(1,len(nums)):
            x=  res[i-1]+nums[i]
            res.append(x)
        return res