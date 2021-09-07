class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        N = len(nums)
        visited = [False] * N
        ans = 0

        for num in nums:
            length = 0
            while not visited[num]:
                visited[num] = True
                length += 1
                num = nums[num]
            ans = max(length, ans)
        return ans

        # Time = O(N)
        # Space = O(N)