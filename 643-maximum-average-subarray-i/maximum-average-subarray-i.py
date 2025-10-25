class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s=0
        for i in range(k):
            s+=nums[i]
        max_ave = s/k
        for i in range(k,len(nums)):
            s += nums[i]
            s -= nums[i-k]
            cur = s/k
            max_ave=max(max_ave,cur)
        return max_ave