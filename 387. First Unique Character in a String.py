class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1

        if len(s) == 1:
            return 0

        res = {}
        for char in s:
            if char not in res:
                res[char] = 1
            else:  # char in res or in counted
                res[char] += 1
        print(res)
        for char, count in res.items():
            if count == 1:
                return s.index(char)
        return -1


    # Time = O(n), Space = O(n)
