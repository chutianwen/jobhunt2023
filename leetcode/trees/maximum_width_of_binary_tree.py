# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        depth_min = defaultdict(lambda: float('inf'))
        depth_max = defaultdict(lambda: float('-inf'))

        # needs to be self. otherwise will have reference problem
        self.max_width = float('-inf')

        def helper(root, depth, idx):
            if not root:
                return

            depth_min[depth] = min(depth_min[depth], idx)
            depth_max[depth] = max(depth_max[depth], idx)

            self.max_width = max(self.max_width, depth_max[depth] - depth_min[depth])

            helper(root.left, depth + 1, idx * 2 - 1)
            helper(root.right, depth + 1, idx * 2)

        helper(root, 0, 1)
        return int(self.max_width) + 1