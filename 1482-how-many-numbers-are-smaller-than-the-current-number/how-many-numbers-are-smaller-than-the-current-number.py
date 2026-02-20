class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = [0 for i in range(len(nums))]
        for i in range(len(nums)):
            cnt = 0
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    cnt+=1
            res[i]=cnt
        # print(res)
        return res

                
        
        
