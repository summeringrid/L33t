def brutal_force(nums, k):
    # brutal force

    n = len(nums)
    while k > 0:
        nums = [nums[-1]] + nums[:n - 1]
        k -= 1
    return nums
    # Time = O(n*k), Space = O(1)


def brutal_forceII(nums, k):
    k %= len(nums)          # only deal with module k part
    for i in range(k):
        previous = nums[-1]
        for j in range(len(nums)):
            nums[j], previous = previous, nums[j]
    return nums
    # Time = O(n*k), Space = O(1)


def rotate(nums, k) -> None:
    n = len(nums)
    a = [0] * n
    for i in range(n):
        a[(i + k) % n] = nums[i]

    nums[:] = a     # HINT: can't accept if without [:]
    return nums
    # Time = O(n)

class Solution:
    def optimized_solution(self, nums, k):
        n = len(nums)
        k %= n

        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1

    # Time = O(n), Space = O(1)



nums = [1,2,3,4,5,6,7]
k = 3

print(rotate(nums, k))