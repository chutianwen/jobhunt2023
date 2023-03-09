# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
#
# The path sum of a path is the sum of the node's values in the path.
#
# Given the root of a binary tree, return the maximum path sum of any non-empty path.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
clas# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = None

        def helper(root):
            if not root:
                return 0

            max_left_path_sum = helper(root.left)
            max_right_path_sum = helper(root.right)

            # only the root itself
            path1 = root.val

            # left path + root
            path2 = max_left_path_sum + root.val

            # right path + root
            path3 = max_right_path_sum + root.val

            # left, root, right
            path4 = max_left_path_sum + root.val + max_right_path_sum

            max_branch = max([path1, path2, path3])
            max_path = max(max_branch, path4)
            if self.res:
                self.res = max(self.res, max_path)
            else:
                self.res = max_path

            return max(max_branch, 0)

        helper(root)
        return self.res