# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right

    # Time = O(n), Space = O(n)


    """
    input:
    [3,1,4,null,2]
    1
    
    Output: None
    Expected: 1
    
    o(╥﹏╥)o Why~~
    
    [update]
    Found the bug, it should be OR not AND when check the cur & stack on line 13
    
    """