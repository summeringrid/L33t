class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        # [1]
        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid

            # [3,4,5,6,0,1,2]
            #  l   m       r
            if nums[mid] >= nums[l]:        # [1,2]
                # left portion or right:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # [5,6,0,1,2,3,4]
            #  l       m   r
            else:
                if target > nums[r] or target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1

        # Time = O(logN)        Space = O(1)



