# Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
#
# For this problem, a height-balanced binary trees is defined as a binary trees in which the depth of the two subtrees of every node never differ by more than 1.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary trees node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        return self.helper(head)

    def helper(self, head):
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        if not head.next.next:
            root = TreeNode(head.next.val)
            leaf = TreeNode(head.val)
            root.left = leaf
            return root

        slow = fast = head
        pre = None
        while fast.next and fast.next.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next

        # slow as mid
        root = TreeNode(slow.val)
        pre.next = None
        left = self.helper(head)
        right = self.helper(slow.next)
        root.left = left
        root.right = right
        return root
