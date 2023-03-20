# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        left_lists, right_lists = self.divide(lists)
        left_sorted_list = self.mergeKLists(left_lists)
        right_sorted_list = self.mergeKLists(right_lists)
        return self.merge(left_sorted_list, right_sorted_list)

    def divide(self, lists):
        mid_idx = len(lists) // 2
        return lists[: mid_idx], lists[mid_idx:]

    def merge(self, left_list, right_list):
        if not left_list or not right_list:
            return left_list or right_list

        dummy_head = ListNode(-1)
        p = dummy_head

        while left_list and right_list:
            if left_list.val <= right_list.val:
                new_node = ListNode(left_list.val)
                left_list = left_list.next
            else:
                new_node = ListNode(right_list.val)
                right_list = right_list.next

            p.next = new_node
            p = p.next

        if left_list:
            p.next = left_list
        if right_list:
            p.next = right_list

        return dummy_head.next

    def _debug(self, list):
        p = ''
        while list:
            p = f'{p} -> {list.val}'
            list = list.next

        print(p)