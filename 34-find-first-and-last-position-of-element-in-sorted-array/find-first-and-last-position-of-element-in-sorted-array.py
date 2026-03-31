class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bisect.bisect_left(nums , target)
        # print(left)
        right = bisect.bisect_right(nums , target)
        # print(right)
        if left < len(nums) and nums[left] == target:
            return [ left , right-1]
        return [-1,-1]

        