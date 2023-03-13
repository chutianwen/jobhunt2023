# Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.
#
# You can return the answer in any order.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque, defaultdict


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        res = []
        if not root or not target:
            return res

        parent_map = defaultdict(TreeNode)

        q = deque([root])
        while q:
            node = q.popleft()
            if node == target:
                continue

            if node.left:
                parent_map[node.left] = node
                q.append(node.left)

            if node.right:
                parent_map[node.right] = node
                q.append(node.right)

        from_target = deque([(target, 0)])

        explored = set()

        while from_target:
            node, distance = from_target.popleft()
            explored.add(node.val)

            if distance > k:
                break
            if distance == k:
                res.append(node.val)

            next_distance = distance + 1

            if node.left and node.left.val not in explored:
                from_target.append((node.left, next_distance))
            if node.right and node.right.val not in explored:
                from_target.append((node.right, next_distance))
            if node in parent_map and parent_map[node].val not in explored:
                from_target.append((parent_map[node], next_distance))

        return res