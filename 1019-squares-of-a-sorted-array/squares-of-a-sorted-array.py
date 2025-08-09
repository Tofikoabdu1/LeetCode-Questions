class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left = 0
        right = n-1
        pos = n-1
        res = [0]*n
        while left <= right:
            left_sq = nums[left]**2
            right_sq = nums[right]**2
            if left_sq > right_sq:
                res[pos] = left_sq
                left+=1
            else :
                res[pos] = right_sq
                right-=1
            pos-=1
        return res
        