"""
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        root.next = None
        # node, depth
        q = deque([(root, 1)])
        pre_right = None
        while q:
            cur, depth = q.popleft()
            depth += 1
            if cur.left and cur.right:
                q.append((cur.left, depth))
                q.append((cur.right, depth))
                cur.left.next = cur.right
                if pre_right:
                    pre_node, pre_depth = pre_right
                    if pre_depth == depth:
                        pre_node.next = cur.left
                    else:
                        pre_node.next = None
                pre_right = (cur.right, depth)
        return root