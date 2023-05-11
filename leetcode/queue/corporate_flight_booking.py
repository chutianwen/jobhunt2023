from collections import defaultdict


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:

        idx_seat_cnt_map = defaultdict(int)

        for first, last, seat_cnt in bookings:
            idx_seat_cnt_map[first - 1] += seat_cnt
            idx_seat_cnt_map[last] -= seat_cnt

        seat_cnt_list = []

        sorted_idx = sorted(idx_seat_cnt_map.keys())

        # append last index as helper
        sorted_idx.append(n)

        pointer = 0
        pre_value = 0
        pre_sorted_idx = 0
        while pointer <= len(sorted_idx) - 1:
            cur_sorted_idx = sorted_idx[pointer]
            seat_cnt_list.extend([pre_value] * (cur_sorted_idx - pre_sorted_idx))
            pre_value += idx_seat_cnt_map[cur_sorted_idx]
            pre_sorted_idx = cur_sorted_idx
            pointer += 1

        return seat_cnt_list