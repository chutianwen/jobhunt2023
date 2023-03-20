# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        original_head = head
        reversed_once_head = None

        pre_head = head
        pre_tail = None
        checked_nodes_cnt = 0
        while head:
            next_head = head.next
            checked_nodes_cnt += 1
            if checked_nodes_cnt == k:
                head.next = None
                reversed_head, reversed_tail = self.reverseList(pre_head)
                if pre_tail:
                    pre_tail.next = reversed_head
                if not reversed_once_head:
                    reversed_once_head = reversed_head
                reversed_tail.next = next_head
                pre_head = next_head
                pre_tail = reversed_tail
                checked_nodes_cnt = 0
            head = next_head

        return reversed_once_head or original_head

    def reverseList(self, head):
        if not head:
            return head, head

        new_head, new_tail = self.reverseList(head.next)
        head.next = None
        if new_tail:
            new_tail.next = head

            return new_head, head
        else:
            return head, head