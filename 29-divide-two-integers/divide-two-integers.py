class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle overflow
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        # Determine sign of result
        negative = (dividend < 0) != (divisor < 0)

        # Work with positive values
        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0

        while dividend >= divisor:
            temp = divisor
            multiple = 1
            # Double temp until it's just below dividend
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            result += multiple

        return -result if negative else result
