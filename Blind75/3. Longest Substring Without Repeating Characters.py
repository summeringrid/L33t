class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Approach I: Deque
        check = deque()
        res = 0

        for c in s:
            while c in check:
                check.popleft()
            else:
                check.append(c)
            res = max(res, len(check))
        return res

        # Time = O(n*res), n = len(s), res = maxLen of the unrepeated substr
        # Space = O(m), m = len(check)

        # Approach II: sliding window
        res = l = 0
        seen = set()
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            res = max(res, r - l + 1)
        return res

        # Time = O(n), n = len(s)
        # Space = O(m), m = len(seen set)