"""
    675874 --> 875674
    678876 --> 878676
    8465473
    89999
    65123789

    left: first increased num and its index
    right: most right greatest num and its index
    if the given num is in decremented order: No swap
"""


class Solution:
    def maximumSwap(self, num: int) -> int:
        num_list = list(str(num))  # Hint1: cast num into str before into list!!! (because integer is not iterable)
        n = len(num_list)

        for i in range(n - 1):  # Hint2: out of boundary
            if num_list[i] < num_list[i + 1]:
                break
        else:
            return num

        max_idx, max_val = i + 1, num_list[i + 1]
        for j in range(i + 1, n):
            if num_list[j] >= max_val:  # Hint3: find the most right max (even same val)
                max_idx, max_val = j, num_list[j]

        left_idx = i
        for k in range(i, -1, -1):  # Hint4: exclusive end should reach 0
            if num_list[k] < max_val:
                left_idx = k

        num_list[left_idx], num_list[max_idx] = num_list[max_idx], num_list[left_idx]

        return int(''.join(num_list))

        # Time, Space = O(N), N = digits of the given num