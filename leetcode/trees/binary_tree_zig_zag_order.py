# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        q = deque([(root, 1)])
        pre_depth = 1
        level_nodes = []

        while q:
            node, depth = q.popleft()
            if depth == pre_depth:
                level_nodes.append(node.val)
            else:

                if pre_depth % 2 == 0:
                    res.append(level_nodes[::-1])
                else:
                    res.append(level_nodes)
                level_nodes = [node.val]

            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))

            pre_depth = depth

        if level_nodes:

            if pre_depth % 2 == 0:
                res.append(level_nodes[::-1])
            else:
                res.append(level_nodes)
        return res