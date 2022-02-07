class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        right = 0
        for c in s:
            if c == "(":
                stack.append(c)
            else:
                if stack:
                    stack.pop()
                else:
                    right += 1

        return right + len(stack)
        # Time = O(N), N = len(s), Space = O(N)

        # Optimized: in-place solution
        need_l = need_r = 0  # record what we missed(need)
        for i in s:
            if need_r == 0 and i == ')':
                need_l += 1
            else:
                need_r += 1 if i == '(' else -1
        return need_l + need_r

        # Time = O(N), Space = O(1)