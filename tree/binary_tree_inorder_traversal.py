# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)

    def inorderTraversalIterative(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res


from collections import deque


class Solution2:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None

        values = deque([])
        while head:
            values.append(head.val)
            head = head.next
        size_tree = len(values)
        root = TreeNode()
        q = deque([root])
        size_tree -= 1
        while size_tree > 0:
            cur = q.popleft()
            size_tree -= 1
            cur.left = TreeNode()
            q.append(cur.left)
            if size_tree > 0:
                size_tree -= 1
                cur.right = TreeNode()
                q.append(cur.right)

        stack = []
        res = root
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            val = values.popleft()
            root.val = val
            root = root.right
        return res

