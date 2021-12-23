class Solution:
    def addBinary(self, a: str, b: str) -> str:

        res = ""
        carry = 0

        a, b = a[::-1], b[::-1]

        for i in range(max(len(a), len(b))):
            digitA = ord(a[i]) - ord('0') if i < len(a) else 0
            digitB = ord(b[i]) - ord('0') if i < len(b) else 0

            total = digitA + digitB + carry
            char = str(total % 2)
            carry = total // 2
            res = char + res

        if carry:
            res = '1' + res  # carry is integer but we need output string
        return res

    # Time = o(n), n is len(a) + len(b)
    # Space = O(n)
    # 67 ===> 415 Add String


def addBinary_ii(a, b) -> str:
    x, y = int(a, 2), int(b, 2)
    print('x=', x, 'y=', y, end='')
    while y:
        answer = x ^ y
        carry = (x & y) << 1
        x, y = answer, carry
    return bin(x)[2:]

a = "11"
b = "1"


print('\nanswer:', addBinary_ii(a, b))

