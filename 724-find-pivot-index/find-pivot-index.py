class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n =len(nums)
        pref = [0]
        for i in range(n):
            pref.append(pref[-1]+nums[i])
        pref.append(0)
        for i in range(1,n+1):
            right = pref[i-1] - pref[0]
            left =pref[n]-pref[i]
            if left == right:
                return i-1
        return -1