class Solution:
    def reverse(self, x: int) -> int:
        """
        Solution 1: convert into string and reverse it; convert back to int
                    note: check out of boundary both on given num and the output result
        """
        MAX = 2 ** 31 - 1
        MIN = -2 ** 31

        if x >= MAX or x <= MIN:
            return 0
        else:
            if x >= 0:
                numStr = str(x)
                result = int(numStr[::-1])
            else:
                numStr = str(x)[1::]
                resultStr = "-" + numStr[::-1]
                result = int(resultStr)
        if result >= MAX or result <= MIN:
            return 0
        else:
            return result

        # Time = O(N), Space=O(1)


    #     """
    #     Solution 2: use fmod to get the last digit; generate the result by *10
    #                 note: check out of boundary before generating the result
    #     """
    #     MAX = 2 ** 31 - 1
    #     MIN = -2 ** 31
    #     result = 0
    #     while x:
    #         # digit = x % 10
    #         digit = int(math.fmod(x, 10))
    #         # x = x // 10
    #         x = int(x / 10)
    #
    #         if result > MAX // 10 or (result == MAX // 10 and digit >= MAX % 10):
    #             return 0
    #
    #         if result < MIN // 10 or (result == MIN // 10 and digit <= MIN % 10):
    #             return 0
    #
    #         result = result * 10 + digit
    #
    #     return result
    #
    # # Time = O(N), Space = O(1)
    #


        # """
        # neater version
        # """
        # num = 0
        # a = abs(x)
        #
        # while a != 0:
        #     temp = a % 10
        #     num = num * 10 + temp
        #     a = int(a / 10)
        #
        # if x > 0 and num < 2147483647:
        #     return num
        # elif x < 0 and num <= 2147483648:
        #     return -num
        # else:
        #     return 0