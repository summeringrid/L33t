class Solution:
    def peakIndexInMountainArray(self, arr) -> int:
        low, high = 0, len(arr) - 1

        # [1, 3, 5, 7, 6, 4,]
        while low < high:
            mid = (low + high) // 2
            if arr[mid] < arr[mid + 1]:
                low = mid + 1
            else:
                high = mid
        return low

    # Time = O(logN), N = len(arr)
