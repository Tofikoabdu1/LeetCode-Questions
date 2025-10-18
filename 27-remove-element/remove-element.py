class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        seek=0
        hold=0
        occur=nums.count(val)
        while seek < len(nums):
            if nums[seek]!=val:
                nums[seek],nums[hold]=nums[hold],nums[seek]
                hold+=1
            # elif nums[seek]==val:
            #     occur+=1
            seek+=1
        return len(nums)-occur


