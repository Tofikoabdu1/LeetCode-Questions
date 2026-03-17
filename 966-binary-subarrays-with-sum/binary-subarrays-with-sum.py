class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = {0: 1}
        current_sum = 0
        total = 0
        for num in nums:
            current_sum += num
            if current_sum - goal in count:
                total += count[current_sum - goal]
            count[current_sum] = count.get(current_sum, 0) + 1
            
        return total