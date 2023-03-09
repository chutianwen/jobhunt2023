# Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value. This path may or may not pass through the root.
#
# The length of the path between two nodes is represented by the number of edges between them.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        self.max = 0

        visited = set()

        def get_depth(root, depth):
            if not root:
                return depth

            visited.add(root)

            left_depth = right_depth = 0

            if root.left and root.left.val == root.val:
                left_depth = get_depth(root.left, depth + 1)

            if root.right and root.right.val == root.val:
                right_depth = get_depth(root.right, depth + 1)

            candidate1 = max([depth, left_depth, right_depth])
            candidate2 = max(left_depth - depth, 0) + max(right_depth - depth, 0)
            self.max = max([self.max, candidate1, candidate2])
            return candidate1

        def traverse(root):
            if not root:
                return

            if root.val not in visited:
                get_depth(root, 0)

            traverse(root.left)
            traverse(root.right)

        traverse(root)
        print(get_depth(root, 0))
        return self.max


class Solution2(object):

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_path = 0

        def dfs(root):

            if not root:
                return 0

            left_length = dfs(root.left)
            right_length = dfs(root.right)

            left_arrow = right_arrow = 0
            if root.left and root.val == root.left.val:
                left_arrow = left_length + 1

            if root.right and root.val == root.right.val:
                right_arrow = right_length + 1

            self.max_path = max(self.max_path, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)

        dfs(root)
        return self.max_path

