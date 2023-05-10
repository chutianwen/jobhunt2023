import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        res = 0
        heap, heap_size = [], 0
        for interval in intervals:
            while heap and heap[0] <= interval[0]:
                heapq.heappop(heap)
                heap_size -= 1
            heapq.heappush(heap, interval[1])
            heap_size += 1
            res = max(res, heap_size)
        return res


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


class EventSolution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        max_needed = 0

        start_events = []
        end_events = []

        for start, end in intervals:
            start_events.append((start, 1))
            end_events.append((end, -1))

        events = start_events + end_events

        # need to make sure [x, -1] is before [x, 1]
        events.sort()
        cnt = 0
        for time_stamp, change in events:
            cnt += change

            max_needed = max(max_needed, cnt)

        return max_needed



