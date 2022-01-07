class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        sCount, pCount = {}, {}

        for i in range(len(p)):
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
            pCount[p[i]] = 1 + pCount.get(p[i], 0)

        res = [0] if sCount == pCount else []

        # l, r: count off index & count in index
        # s = "cbaebabacd", p = "abc"
        #      ↑  ↑
        l = 0
        for r in range(len(p), len(s)):
            sCount[s[r]] = 1 + sCount.get(s[r], 0)
            sCount[s[l]] -= 1

            if sCount[s[l]] == 0:
                sCount.pop(s[l])

            l += 1
            # THE PLACE WHERE TO UPDATE L POINTER IS VERY IMPORTANT

            if sCount == pCount:
                res.append(l)

        return res

    # because we just see the size of each unique charactor
    # Space = O(26)
    # Time = O(n), n = max(len(s), len(p))