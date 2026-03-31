class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(x):
            curr = 1
            curr_w = 0
            for i in weights:
                if curr_w + i > x:
                    curr +=1
                    curr_w = 0
                curr_w += i
            if curr <= days:
                return True
            else:
                return False

        left = max(weights)
        right = sum(weights)
        ans = left
        while left<=right:
            mid = (left+right)//2
            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

        