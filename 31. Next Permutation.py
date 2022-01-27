class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [ 2, 3, 4, 6, 5]  --> [2, 3, 5, 4, 6]
        #            i
        #               j
        #         k
        # [ 2, 3, 5, 6, 4]
        # [2, 3, 4, 9, 8, 7, 5, 1]  --> [2, 3, 5, 1, 4, 7, 8, 9]
        #           i

        i = j = len(nums) - 1  # last index
        while i > 0 and nums[i - 1] >= nums[i]:  # HINT: i can't be equal to 0 here
            i -= 1

        if i == 0:  # the nums is in descending order
            nums.reverse()
            return

        k = i - 1  # the last 'ascending' element
        while nums[j] <= nums[k]:
            j -= 1
        nums[j], nums[k] = nums[k], nums[j]

        l, r = k + 1, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        # O(n)    otpimize:  --> binary search to find the swap point

        i = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1

        #         if i == 0:
        #             nums.reverse()
        #             return
        if i > 0:  # if add this part, no need to use built-in reverse
            l, r = i, len(nums) - 1
            while l <= r:
                # mid = (l + r) // 2            # HINT: here the mid index has a init starting pos
                mid = l + (r - l) // 2
                if nums[i - 1] < nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
                # l and right meet each other: swap i-1 & l or r - 1 (because we want the most nearest bigger one)
            nums[i - 1], nums[l - 1] = nums[l - 1], nums[i - 1]

        # reverse the rest part starting at index i
        left, right = i, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        # Time = O(m + logm), m is the length of the descending part on the right








