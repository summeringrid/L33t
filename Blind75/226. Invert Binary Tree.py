# basic concept of deque in collections
import collections
from collections import deque

# Declaring deque
queue = deque(['name', 'age', 'DOB'])
queue.appendleft('start')
queue.append('company')
print(queue)
print(queue.pop())          # stack - LILO
print(queue.popleft())      # queue - FILO




# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        # DFS - recursivelly solve the prob
        # Time = O(n) n is the number of the node
        # Space = O(h), h is the height of the tree
        #         if not root:
        #             return None
        #         tmp = root.left
        #         root.left = root.right
        #         root.right = tmp

        #         self.invertTree(root.left)
        #         self.invertTree(root.right)
        #         return root

        #         # traditional DFS template (stack)
        #         stack = []
        #         stack.append(root)
        #         while stack:
        #             node = stack.pop()
        #             if node:
        #                 node.left, node.right = node.right, node.left
        #                 stack.append(node.left)
        #                 stack.append(node.right)
        #         return root

        # BFS - iteratively solve the prob
        # Time = O(n) n is the num of nodes
        # Space = O(n) cuz worst case the tree will contains all nodes in one level

        if not root:
            return None
        # queue = collections.deque(root)
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                node.left, node.right = node.right, node.left
                queue.extend([node.left, node.right])
        return root
