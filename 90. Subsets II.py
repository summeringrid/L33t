class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtracking(i, cur):
            if i == len(nums):
                res.append(cur[:])
                return

            cur.append(nums[i])
            backtracking(i + 1, cur)
            cur.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtracking(i + 1, cur)

        backtracking(0, [])

        return res

    # Time = O(N * 2^N) generate all subsets and then copy them into output list
    # Space = O(N)  maintain cur and modify cur in-place with backtracking