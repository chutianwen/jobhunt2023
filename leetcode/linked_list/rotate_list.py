# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        length_list, tail = self.traverse(head)

        steps_to_new_head = length_list - k % length_list

        # return new head, connect old head to old tail
        if steps_to_new_head in (0, length_list):
            return head
        else:
            new_head = head
            for idx in range(steps_to_new_head):
                next_head = new_head.next
                if idx == steps_to_new_head - 1:
                    new_head.next = None
                new_head = next_head
            tail.next = head
            return new_head

    def traverse(self, head):
        cnt = 0
        tail = None
        while head:
            cnt += 1
            if not head.next:
                tail = head
            head = head.next
        return cnt, tail
