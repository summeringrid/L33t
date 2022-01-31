class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            #  4,5,6,7,0,1,2,3]
            #  l       m   t r

            #  5,6,7,0,1,2,3,4]
            #  l t   m   t'  r
            #  l       t m   r

            if nums[mid] < nums[l]:
                if target > nums[r] or target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1


            # [4,5,6,7,8,0,1,2,3]
            #  l     m         r
            else:
                if target > nums[mid] or target < nums[l]:  # ※ HINT: not nums[r]
                    l = mid + 1
                else:
                    r = mid - 1
        return -1