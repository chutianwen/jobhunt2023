'''
Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        res = None
        pre = None
        while head and head.next:
            if pre:
                pre.next = head.next

            pre = head

            if res is None:
                res = head.next

            tmp = head.next.next
            head.next.next = head
            head.next = tmp
            head = tmp

        return res or head