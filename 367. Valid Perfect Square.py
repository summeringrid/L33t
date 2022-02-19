class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        # Time = O(sqt())

        for i in range(1, num + 1):
            if i * i == num:
                return True
            if i * i > num:
                return False

        # Time = O(logn)

        l, r = 1, num
        while l <= r:
            mid = (l + r) // 2
            if mid * mid > num:
                r = mid - 1
            elif mid * mid < num:
                l = mid + 1
            else:
                return True
        return False