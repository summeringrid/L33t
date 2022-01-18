# Brutal Force
class Solution:
    def findMaxAverage(self, nums, k):
        result = float('-inf')
        for i in range(k, len(nums) + 1):
            result = max(result, self.get_max_average(nums, i))
        return result

    def get_max_average(self, nums, k):
        if len(nums) < k:
            return 0.0
        max_so_far = sum_so_far = sum(nums[:k])
        for i in range(k, len(nums)):
            sum_so_far = sum_so_far + nums[i] - nums[i - k]
            max_so_far = max(max_so_far, sum_so_far)
        return float(max_so_far) / k

        # Time = O(n^2) ----------- TLE Error


# Binary Search
class Solution:
    def findMaxAverage(self, nums, k):
        if not nums:
            return 0

        start, end = min(nums), max(nums)
        while end - start > 1e-5:
            mid = (start + end) / 2
            if self.can_process(nums, k, mid):
                start = mid
            else:
                end = mid

        return start

    def can_process(self, nums, k, average):
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num - average)

        min_prefix_sum = 0
        for i in range(k, len(nums) + 1):
            if prefix_sum[i] - min_prefix_sum >= 0:
                return True
            min_prefix_sum = min(min_prefix_sum, prefix_sum[i - k + 1])
        return False

    # Time = O(Nlog(max_nums - min_nums)
    # Space = O(1)


# O(n) optimized solution ---------------- Convex Hull Window
class Solution:
    def findMaxAverage(self, nums, k):

        N = len(nums)
        prefix_sum = [0]
        for num in nums:
            P.append(P[-1] + num)

        # helper(i, j) = (nums[i]+...+nums[j]) / (j-i+1)
        def helper(i, j):
            return (prefix_sum[j + 1] - prefix_sum[i]) / float(j + 1 - i)

        hull = collections.deque()  # density
        ans = float('-inf')

        for i in range(k - 1, N):
            while len(hull) >= 2 and helper(hull[-2], hull[-1] - 1) >= helper(hull[-2], i - k):
                hull.pop()
            hull.append(i - k + 1)
            while len(hull) >= 2 and helper(hull[0], hull[1] - 1) <= helper(hull[0], i):
                hull.popleft()
            ans = max(ans, helper(hull[0], i))

        return ans
