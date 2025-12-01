class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        min_len = float('inf')
        cur_sum = 0
        for i in range(n):
            l = i+1
            r = n-1
            while l < r:
                s = nums[i]+nums[l]+nums[r]
                if s == target:
                    return s
                d = abs(target - s)
                min_len =min(min_len , d)
                if min_len == d:
                    cur_sum=s
                if s < target:
                    l +=1
                else:
                    r-=1
        return cur_sum