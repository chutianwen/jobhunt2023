# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        #  map key: encoded value, value: node val. Using in-order
        encode_node_map = defaultdict(list)

        def traverse(root):
            if not root:
                return 'N'

            left_encode = traverse(root.left)
            right_encode = traverse(root.right)

            full_encode = f'L:{left_encode}M:{root.val}R:{right_encode}'
            encode_node_map[full_encode].append(root)

            return full_encode

        traverse(root)

        res = []
        for key, nodes in encode_node_map.items():
            if len(nodes) > 1:
                # print(key, nodes)
                res.append(nodes[0])

        return res



