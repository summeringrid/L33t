class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        index_to_remove = set()
        left_par_stack = []

        for i, c in enumerate(s):
            if c not in "()":
                continue
            if c == "(":
                left_par_stack.append(i)
            elif not left_par_stack:
                index_to_remove.add(i)
            else:  # met a ")"
                left_par_stack.pop()

        index_to_remove = index_to_remove.union(set(left_par_stack))

        string_builder = []

        for i, c in enumerate(s):
            if i not in index_to_remove:
                string_builder.append(c)
        return "".join(string_builder)

    # Time = O(n), n = len(s)
    # Space = O(n)

