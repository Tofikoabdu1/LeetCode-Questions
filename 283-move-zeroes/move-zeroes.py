class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hold = 0
        seek = 0
        while seek < len(nums):
            if nums[seek] != 0:
                nums[seek],nums[hold] = nums[hold],nums[seek]
                hold+=1
            seek+=1
        