# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        encode = [str(root.val)]
        q = deque([root])
        none_token = '$'

        while q:
            cur_node = q.popleft()
            if cur_node.left:
                encode.append(str(cur_node.left.val))
                q.append(cur_node.left)
            else:
                encode.append(none_token)

            if cur_node.right:
                encode.append(str(cur_node.right.val))
                q.append(cur_node.right)
            else:
                encode.append(none_token)

        return ','.join(encode)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        q = deque([root])
        cur_idx = 1
        while q:
            cur_node = q.popleft()

            if nodes[cur_idx] != '$':
                left_node = TreeNode(int(nodes[cur_idx]))
                q.append(left_node)
                cur_node.left = left_node
            cur_idx += 1

            if nodes[cur_idx] != '$':
                right_node = TreeNode(int(nodes[cur_idx]))
                q.append(right_node)
                cur_node.right = right_node
            cur_idx += 1

        return root
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))