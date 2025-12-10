class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        arr =[nums[0]]
        for num in nums[1:]:
            if num != arr[-1]:
                arr.append(num)
        nums = arr    
        count =0
        for i in range(1,len(arr)-1):
            if nums[i-1]<nums[i] and nums[i]>nums[i+1]:
                count+=1
            elif  nums[i-1]>nums[i] and nums[i]<nums[i+1]:
                count +=1
        return count
