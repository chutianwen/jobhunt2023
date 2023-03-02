# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary trees. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary trees can be serialized to a string and this string can be deserialized to the original trees structure.
#
# Clarification: The input/output format is the same as how LeetCode serializes a binary trees. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

# Definition for a binary trees node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Codec:
    null = '#'

    def serialize(self, root):
        """Encodes a trees to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        q = deque([root])
        res = f'{root.val}'
        while q:
            cur = q.popleft()
            if cur.left:
                res += f',{cur.left.val}'
                q.append(cur.left)
            else:
                res += f',{Codec.null}'
            if cur.right:
                res += f',{cur.right.val}'
                q.append(cur.right)
            else:
                res += f',{Codec.null}'
        return res

    def deserialize(self, data):
        """Decodes your encoded data to trees.

        :type data: str
        :rtype: TreeNode
        """

        if data:
            items = deque(data.split(","))
            head = items.popleft()
            root = TreeNode(head)
            q = deque([root])
            while items:
                cur = q.popleft()
                left = items.popleft()
                right = items.popleft()
                if left != Codec.null:
                    cur.left = TreeNode(left)
                    q.append(cur.left)
                if right != Codec.null:
                    cur.right = TreeNode(right)
                    q.append(cur.right)
            return root
        else:
            return None

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))