class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False        # why? -9 is (-3)**3 as well!!

        while n % 3 == 0:
            n /= 3

        return True if n == 1 else False
        # return True   ❌

        # Time = O(log3 n)
        # Space = O(log3 n)

    # Follow up: Could you solve it without loops/recursion?

        # return n > 0  and 2147483646 % n == 0   ❌
        return n > 0 and 1162261467 % n == 0  # the max of int power of 3 i.e 1162261467.

    # Time = Space = O(1)