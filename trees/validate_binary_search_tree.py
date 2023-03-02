# Definition for a binary trees node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        is_bst, _, _ = self.helper(root)
        return is_bst

    # method return (min, max, isBST)
    def helper(self, root: Optional[TreeNode]):
        # print(root)
        if root and root.left is None and root.right is None:
            return True, root.val, root.val

        flag_left = flag_right = True
        if root.left:
            left_is_bst, left_min, left_max = self.helper(root.left)
            if not left_is_bst:
                return False, None, None
            flag_left = root.val > root.left.val and root.val > left_max
        else:
            left_min = root.val

        if root.right:
            right_is_bst,  right_min, right_max = self.helper(root.right)
            if not right_is_bst:
                return False, None, None
            # print(left_min, left_max, right_min, right_max)
            flag_right = root.val < root.right.val and root.val < right_min
        else:
            right_max = root.val

        return flag_left == flag_right == True, left_min, right_max