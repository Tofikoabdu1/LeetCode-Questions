class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        j = 1
        left = 0
        max_len = 0
        for right in range(len(nums)):
            while j == 0 and nums[right] == 0:
                if nums[left] == 0:
                    j+=1
                left+=1
            if nums[right] == 0:
                j-=1
            max_len = max(max_len , right -left)
        return max_len

        