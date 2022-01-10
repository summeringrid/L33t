class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # Approach I: group all the repeated binary digit
        # i.e. s = "00110011"
        # group  = [2,2,2,2]
        #           ^ ^
        #             ^ ^
        #               ^ ^
        if not s:
            return 0
        group = [1]
        for i in range(1, len(s)):
            if s[i - 1] != s[i]:
                # they should be divided into two groups
                group.append(1)
            else:
                # meet same digit, should count into the same group
                group[-1] += 1
        ans = 0
        for i in range(1, len(group)):
            ans += min(group[i - 1], group[i])
        return ans

        # Time = O(n)

        # optimized: one pass iteration -> two pointers
        # i.e. s = "0011100011"
        #           01
        #            11
        #             12
        #              23
        #               31
        #                32

        ans = 0
        prev, cur = 0, 1
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                ans += min(prev, cur)
                prev, cur = cur, 1
            else:
                cur += 1
        return ans + min(prev, cur)



