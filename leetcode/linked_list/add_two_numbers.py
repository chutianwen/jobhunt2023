# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        remaining = 0

        p1, p2 = l1, l2

        while p1 and p2:
            cur_sum = p1.val + p2.val + remaining

            p1.val = cur_sum % 10
            remaining = cur_sum // 10

            if not p1.next or not p2.next:
                break
            p1 = p1.next
            p2 = p2.next

        if p1.next is None:
            p1.next = p2.next

        while p1.next:
            cur_sum = p1.next.val + remaining
            p1.next.val = cur_sum % 10
            remaining = cur_sum // 10
            p1 = p1.next

        if remaining != 0:
            p1.next = ListNode(remaining)

        return l1

class Solution2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 or not l2:
            return 1 or l2

        p1 = l1
        p2 = l2

        left_over = 0

        while p1 and p2:
            cur_sum = p1.val + p2.val + left_over
            p1.val = cur_sum % 10
            left_over = cur_sum // 10

            if not p1.next or not p2.next:
                break

            p1 = p1.next
            p2 = p2.next

        if not p1.next and not p2.next:
            p1.next = ListNode(left_over) if left_over == 1 else None
            return l1

        if not p1.next and p2.next:
            p1.next = p2.next

        p1 = p1.next
        while p1:
            cur_sum = p1.val + left_over
            p1.val = cur_sum % 10
            left_over = cur_sum // 10

            if not p1.next:
                p1.next = ListNode(left_over) if left_over == 1 else None
                return l1
            p1 = p1.next




