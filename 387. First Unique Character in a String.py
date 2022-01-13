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


class Solution2:
    def firstUniqChar(self, s: str) -> int:
        dict = collections.defaultdict(int)

        for char in s:
            dict[char] += 1

        for i, c in enumerate(s):
            if dict[c] < 2:
                return i
        return -1

    # one pass
    def firstUniqChar2(self, s: str) -> int:
        d = collections.defaultdict(int)
        seen = set()

        for i, c in enumerate(s):
            if c not in seen:
                d[c] = i
                seen.add(c)
            elif c in d:  # c in seen and in d
                del d[c]
        return min(d.values()) if d else -1
