class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(capacity: int) -> bool:
            current_weight = 0
            required_days = 1
            for weight in weights:
                if current_weight + weight > capacity:
                    required_days += 1
                    current_weight = 0
                current_weight += weight
            return required_days <= days

        low = max(weights)
        high = sum(weights)
        result = high

        while low <= high:
            mid = (low + high) // 2
            if canShip(mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1

        return result


            
        