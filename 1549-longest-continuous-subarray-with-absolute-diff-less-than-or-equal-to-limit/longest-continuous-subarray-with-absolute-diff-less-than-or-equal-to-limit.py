class Solution:
    def longestSubarray(self, nums, limit):
        max_q = deque()
        min_q = deque()
        left = 0
        ans = 0

        for right in range(len(nums)):
            while max_q and nums[right] > max_q[-1]:
                max_q.pop()
            max_q.append(nums[right])

            while min_q and nums[right] < min_q[-1]:
                min_q.pop()
            min_q.append(nums[right])

            while max_q[0] - min_q[0] > limit:
                if nums[left] == max_q[0]:
                    max_q.popleft()
                if nums[left] == min_q[0]:
                    min_q.popleft()
                left += 1

            ans = max(ans, right - left + 1)

        return ans