class Solution:
    def hammingWeight(self, n: int) -> int:
        # # Approach 1
        # res = 0
        # while n:
        #     res += n % 2
        #     n = n >> 1
        # return res

        # Time = O(1)， most run time is 32
        # Space = O(1)

        # # Approach 2
        res = 0
        while n:
            n &= (n - 1)
            res += 1
        return res
