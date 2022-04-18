class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX, MIN = 2 ** 31 - 1, -2 ** 31
        positive = (dividend < 0) is (divisor < 0)  # positive = dividend < 0 == divisor< 0
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                temp <<= 1
                i <<= 1
        ##############################################
        # x = 0
        # while dividend >= divisor << (x + 1): x += 1
        # res += 1 << x
        # dividend -= divisor << x
        if not positive:
            res = -res

        return min(MAX, max(MIN, res))
