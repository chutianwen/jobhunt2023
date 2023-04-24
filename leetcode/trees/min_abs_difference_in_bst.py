# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        # each sub node return a head, tail, and compare with current node.

        self.min_abs_value = float('inf')

        def head_tail(root):
            if not root:
                return None, None

            left_head, left_tail = head_tail(root.left)
            right_head, right_tail = head_tail(root.right)

            left_comparator = left_tail or left_head
            right_comparator = right_head or right_tail

            if left_comparator is not None:
                self.min_abs_value = min(self.min_abs_value, abs(left_comparator - root.val))
            if right_comparator is not None:
                self.min_abs_value = min(self.min_abs_value, abs(right_comparator - root.val))

            return left_head or left_tail or root.val, right_tail or right_head or root.val

        h, t = head_tail(root)
        # print(h, t)

        if self.min_abs_value == float('inf'):
            return 0
        else:
            return self.min_abs_value