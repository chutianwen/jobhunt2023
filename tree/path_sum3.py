# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.
#
# A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        if not root.left and not root.right:
            if root.val == targetSum:
                return [[root.val]]
            else:
                return []
        else:
            left_pathes = self.pathSum(root.left, targetSum - root.val)
            right_pathes = self.pathSum(root.right, targetSum - root.val)
            res = []
            for path in left_pathes + right_pathes:
                path_new = [root.val] + path
                res.append(path_new)

            return res


from collections import deque


class Solution2:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        if not root:
            return []
        q = deque([(root, [root.val], root.val)])
        res = []
        while q:
            cur, path, path_sum = q.popleft()
            if not cur.left and not cur.right and path_sum == targetSum:
                res.append(path)
                continue
            if cur.left:
                q.append((cur.left, path + [cur.left.val], path_sum + cur.left.val))
            if cur.right:
                q.append((cur.right, path + [cur.right.val], path_sum + cur.right.val))
        return res