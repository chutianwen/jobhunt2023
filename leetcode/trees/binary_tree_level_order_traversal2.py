# Given the root of a binary trees, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).

# Definition for a binary trees node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque([(root, 1)])
        pre = None
        while q:
            cur, depth = q.popleft()
            if pre:
                pre_node, pre_depth = pre
                if pre_depth == depth:
                    res[-1].append(cur.val)
                else:
                    res.append([cur.val])
            else:
                res.append([cur.val])
            pre = (cur, depth)

            if cur.left:
                q.append((cur.left, depth + 1))

            if cur.right:
                q.append((cur.right, depth + 1))

        return res[::-1]