# Approach I: linear solution ====================================
from collections import deque
from itertools import islice


def linear_solution(arr, x, k):
    # Trivial cases
    if x <= arr[0]:
        return arr[0:k]
    elif x >= arr[-1]:
        return arr[-k:]

    it = iter(nums)
    sliding_window = deque(islice(it, k), maxlen=k)

    for arr in it:
        if abs(x-arr) < abs(x-sliding_window[0]):
            sliding_window.append(arr)
    return [arr for arr in sliding_window]

    # Time = O(N)


# Approach II: binary solution ====================================

def binary_solution(arr, x, k):
    pass

# Time = O(logN + k) --> optimize (logN) -> log(N-k)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 5
k = 4

print('linear search result:\n', linear_solution(nums, x, k), sep='')
# print('binary search result:\n', binary_solution(nums, x, k), sep='')
