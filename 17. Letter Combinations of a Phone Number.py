class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtracking(i, curStr):  # cur digit & cur constructed str
            if len(curStr) == len(digits):
                res.append(curStr)
                return

            for c in digitToChar[digits[i]]:
                backtracking(i + 1, curStr + c)

        if digits:
            backtracking(0, '')

        return res

        # Time = O(N * 4^N)