class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # brutal force

        prefix = strs[0]

        for i in range(1, len(strs)):
            while not strs[i].startswith(prefix):
                prefix = prefix[0:-1]
        return prefix

        # Time = O(n * m), n = len(strs), m = len(first word)

        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res

        # Time = O(n * m), n = len(strs), m = len(first word)