class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            L = i+1
            R = n-1
            while L < R:
                s = nums[L] + nums[R]
                if s == (-1*nums[i]):
                    ans.append([nums[i],nums[L],nums[R]])
                    L += 1
                    while nums[L] == nums[L-1] and L < R:
                        L+=1
                elif s < (-1*nums[i]):
                    L += 1
                else:
                    R -= 1
        return ans
                
                
        