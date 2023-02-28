# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        q = deque([(root, 1)])
        pre = None
        while q:
            cur, depth = q.popleft()
            if pre:
                pre_node, pre_depth = pre
                if pre_depth == depth:
                    pre_node.next = cur
            pre = (cur, depth)
            depth += 1
            pre_node, pre_depth = pre
            if cur.left:
                q.append((cur.left, depth))
            if cur.right:
                q.append((cur.right, depth))
        return root