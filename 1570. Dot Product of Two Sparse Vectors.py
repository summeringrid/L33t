class SparseVector:
# Approach I =======================
    def __init__(self, nums: List[int]):
        self.nums = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        product = 0

        for n1, n2 in zip(self.nums, vec.nums):
            product += n1 * n2
        return product

    # Time = O(n), Space = O(1)

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

# Approach II =======================
    # Use hashmap to store the non-zero val in the v1, only calculate and add these indeces at v2
    # still use O(n) Time, Space cost is O(L), L is the length of the non-zero num in the vector arrary
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.nonzero = {}  # mapping index to non-zero val
        for i, n in enumerate(nums):
            if n != 0:
                self.nonzero[i] = n

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for i, n in vec.nonzero.items():
            if i in self.nonzero:
                res += self.nonzero[i] * n
        return res

    # Time = O(N), Space = O(M), N is nums length, M is nonzero num