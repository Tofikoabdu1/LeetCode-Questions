class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def recur(i, j):
            if i == j:
                return nums[i]
            
            l = nums[i] - recur(i + 1, j)
            r = nums[j] - recur(i, j - 1)
            
            return max(l, r)
        
        return recur(0, len(nums) - 1) >= 0