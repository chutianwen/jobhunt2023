# One way to serialize a binary tree is to use preorder traversal. When we encounter a non-null node,
# we record the node's value. If it is a null node, we record using a sentinel value such as '#'.
# For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where '#' represents a null node.
#
# Given a string of comma-separated values preorder, return true if it is a correct preorder traversal serialization of a binary tree.
#
# It is guaranteed that each comma-separated value in the string must be either an integer or a character '#' representing null pointer.
#
# You may assume that the input format is always valid.
#
# For example, it could never contain two consecutive commas, such as "1,,3".
# Note: You are not allowed to reconstruct the tree.

from collections import deque


class Solution:
    null = "#"

    def isValidSerialization(self, preorder: str) -> bool:
        items = deque(preorder.split(','))
        return self.helper(items) and len(items) == 0

    def helper(self, items):
        if not items:
            return False

        item = items.popleft()
        if item == Solution.null:
            return True

        return self.helper(items) and self.helper(items)


class Solution2:
    def isValidSerialization(self, preorder: str) -> bool:

        nums = 0
        popped = 0
        stack = []
        preorder = preorder.split(",")

        for i in preorder:
            if i.isdigit():
                nums += 1

        for i, val in enumerate(preorder):
            if val.isdigit():
                stack.append(val)
            elif val == "#" and stack and i < len(preorder) - 1:
                stack.pop()
                popped += 1
            elif val == '#' and i == len(preorder) - 1 and len(stack) == 0:
                break
            else:
                return False

        return nums == popped


from collections import deque


class Solution3:
    null = "#"

    def isValidSerialization(self, preorder: str) -> bool:

        if not preorder:
            return True

        q = deque(preorder.split(","))
        stack = []
        root = q[0]

        while root != Solution.null or stack:
            while q and q[0] != Solution.null:
                root = q.popleft()
                stack.append(root)

            # left
            if q and q[0] == Solution.null:
                q.popleft()
            else:
                return False

            # right
            if q:
                root = q[0]
            else:
                return False
            stack.pop()
        return len(q) == 0 or (len(q) == 1 and q[0] == Solution.null)