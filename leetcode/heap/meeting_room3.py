import heapq


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:

        meetings.sort(key=lambda x: x[0])

        # (expire, room_idx)
        heap = []
        cnt = [0] * n
        unused_rooms = set(range(n))

        for left, right in meetings:
            while heap and heap[0][0] <= left:
                _, room_idx = heapq.heappop(heap)
                unused_rooms.add(room_idx)

            if len(unused_rooms) == 0:
                earlist_expire, room_idx = heapq.heappop(heap)
                heapq.heappush(heap, (earlist_expire + right - left, room_idx))
                cnt[room_idx] += 1
            else:
                min_unused_room_idx = min(unused_rooms)
                heapq.heappush(heap, (right, min_unused_room_idx))
                cnt[min_unused_room_idx] += 1
                unused_rooms.remove(min_unused_room_idx)

        # print(cnt)
        max_cnt = 0
        max_cnt_room_idx = None

        for room_idx, room_cnt in enumerate(cnt):
            if max_cnt < room_cnt:
                max_cnt_room_idx = room_idx
                max_cnt = room_cnt

        return max_cnt_room_idx