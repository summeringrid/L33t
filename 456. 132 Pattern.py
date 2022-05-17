class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []  # pair [num, minLeft]
        curMin = nums[0]

        for n in nums[1:]:  # potential k
            while stack and n >= stack[-1][0]:
                stack.pop()
            if stack and n > stack[-1][1]:
                return True
            stack.append(([n, curMin]))
            curMin = min(curMin, n)
        return False

    # Time = O(n), Space = O(1)