class Solution(object):
    def checkSubarraySum(self, nums, k):
        if not nums:
            return False
        pref = 0
        d = {0: -1}
        for i, num in enumerate(nums):
            pref += num
            r = pref % k
            if r in d:
                if i - d[r] > 1:
                    return True
            else:
                d[r] = i
        return False