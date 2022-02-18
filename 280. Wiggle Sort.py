class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # sorted -> swap odd index with its following index
        # Time = O(NlogN + N)

        # --> Time = O(N)
        # nums = [3,5,2,1,6,4]
        # output=[3,5,1,6,2,4]
        if not nums: return
        for i in range(1, len(nums), 2):
            if nums[i] < nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
            # odd index num is greater than its previous index num
            if i + 1 < len(nums) and nums[i] < nums[i + 1]:  # compare with following num
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

        return nums