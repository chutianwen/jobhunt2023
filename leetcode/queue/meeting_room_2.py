import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        sorted_intervals = sorted(intervals)

        # using a heap to store each meeting room expiration time, check with one with earliest
        meeting_heap = []

        for start, end in sorted_intervals:
            if not meeting_heap:
                meeting_heap.append(end)
            else:
                # earliest one still not available
                if start < meeting_heap[0]:
                    heapq.heappush(meeting_heap, end)
                else:
                    earliest_available = heapq.heappop(meeting_heap)
                    # update this meeting room with current end.
                    heapq.heappush(meeting_heap, end)

        return len(meeting_heap)


