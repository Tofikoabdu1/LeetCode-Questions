class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0 or k == 1:
            return 0
        temp = 1
        l = 0
        count = 0
        for r in range(len(nums)):
            temp *= nums[r]
            while(l <= r and temp >= k):
                temp//=nums[l]
                l+=1
            count+=(r-l + 1)
        return count




        
        