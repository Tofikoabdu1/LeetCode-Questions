class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        s = sorted(nums)
        res = []
        for i in nums:
            x = s.index(i)
            res.append(x)
        return res
