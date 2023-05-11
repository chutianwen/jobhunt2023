import bisect


class MyCalendarThree:

    def __init__(self):
        self.events = []

    def book(self, startTime: int, endTime: int) -> int:
        start_event = (startTime, 1)
        end_event = (endTime, -1)

        bisect.insort(self.events, start_event)
        bisect.insort(self.events, end_event)

        max_room_needed = 0
        room_cnt = 0
        for _, change in self.events:
            room_cnt += change
            max_room_needed = max(max_room_needed, room_cnt)

        return max_room_needed

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)