class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # s = "PAYPALISHIRING"
        # numRows = 4, L = ['PIN', 'ALSIG', 'YAHR', 'PI']
        # index = 0   -> L[0] += P
        # index = 1   -> L[1] += A
        # index = 2   -> L[2] += Y
        # index = 3   -> L[3] += P    index == numRows-1   -> step = -1 -> index = 2
        # index = 2   -> L[2] += A                            step = -1 -> index = 1
        # index = 3   -> L[1] += L                            step = -1 -> index = 0
        # index = 2   -> L[0] += I                            step =  1 -> index = 1
        # index = 3   -> L[1] += S                            step =  1 -> index = 2
        # index = 2   -> L[2] += H                            step =  1 -> index = 3
        # index = 3   -> L[3] += I    index == numRows-1   -> step = -1 -> index = 2
        # index = 2   -> L[2] += R                            step = -1 -> index = 1
        # index = 3   -> L[1] += I                            step = -1 -> index = 0
        # index = 2   -> L[0] += N                            step =  1 -> index = 1
        # index = 3   -> L[1] += G

        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows  # e.g. numRows = 3: L = ['', '', '', '']

        index, step = 0, 1
        for x in s:
            L[index] += x

            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1

            index += step
        return ''.join(L)
    d