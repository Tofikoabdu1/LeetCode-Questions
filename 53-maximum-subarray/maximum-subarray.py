class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        curr =0
        for i in range(len(nums)):
            curr += nums[i]
            max_sum = max(max_sum , curr)
            if curr < 0:
                curr=0
        return max_sum
        