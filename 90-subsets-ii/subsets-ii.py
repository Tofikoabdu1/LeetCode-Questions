class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def back(idx , arr):
            if idx == len(nums):
                res.append(arr[::])
                return
            arr.append(nums[idx])
            back(idx+1 , arr)
            arr.pop()
            while idx+1 < len(nums) and nums[idx] == nums[idx+1]:
                idx+=1
            back(idx+1 , arr)
        back(0 , [])
        return res
        