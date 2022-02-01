class Solution:
    def simplifyPath(self, path: str) -> str:
        # . curr dir
        # .. up dir
        # // == /
        # ... dir

        cur = ""
        stack = []
        for c in path + '/':
            if c == '/':
                if cur == '..':
                    if stack: stack.pop()
                elif cur != '' and cur != '.':
                    stack.append(cur)
                cur = ""
            else:
                cur += c

        return '/' + '/'.join(stack)

    # Time = O(n), Space = O(n)