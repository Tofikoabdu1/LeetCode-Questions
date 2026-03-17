class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref_counts = {0: 1}
        current_pref = 0
        cnt = 0
        for i in range(len(nums)):
            current_pref += nums[i]
            target = current_pref - k
            if target in pref_counts:
                cnt += pref_counts[target]
            pref_counts[current_pref] = pref_counts.get(current_pref, 0) + 1 
        return cnt