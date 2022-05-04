class Solution:
    def canJump(self, nums: List[int]) -> bool:
        can_reach = 0
        for idx, num in enumerate(nums):
            if idx > can_reach:
                return False
            can_reach = max(can_reach, idx + num)
        return True

    # Time = O(n)
    # Space = O(1)


    # Approach II:
    goal = len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] + i >= goal:
            goal = i
    return not goal     # first num is not 0


nums = [2,3,1,1,4]
for i in range(len(nums), -1, -1):      # 5,4,3,2,1,0
    print(i)
print('===')
for j in range(len(nums))[::-1]:        # 4,3,2,1,0
    print(j)