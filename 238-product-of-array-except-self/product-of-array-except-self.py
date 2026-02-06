class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        x = 1
        zero = 0
        for i in nums:
            if i == 0:
                zero+=1
        if zero > 1:
            return [0]*len(nums)
        for i in nums:
            if i != 0:
                x*=i
        res = []
        for i in nums:
            if i == 0:
                res.append(x)
            elif i != 0 and zero == 0:
                res.append(x//i)
            else:
                res.append(0)
        return res
