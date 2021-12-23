class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        carry = 0
        num1, num2 = num1[::-1], num2[::-1]

        for i in range(max(len(num1), len(num2))):
            digitA = ord(num1[i]) - ord('0') if i < len(num1) else 0
            digitB = ord(num2[i]) - ord('0') if i < len(num2) else 0

            total = digitA + digitB + carry

            char = str(total % 10)
            carry = total // 10
            res = char + res
        if carry:
            carry = str(carry)
            res = carry + res
        return res

        # Time = O(M+N), M=len(num1), N=len(num2)
        # Space = O(M+N)
        # 67. Add Binary <=== 415