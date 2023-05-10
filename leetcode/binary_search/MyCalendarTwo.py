import bisect

class MyCalendarTwo:
    def __init__(self):
        self.lst = []

    def book(self, start, end):
        bisect.insort(self.lst, (start, 1))
        bisect.insort(self.lst, (end, -1))
        booked = 0
        for time, n in self.lst:
            booked += n
            if booked == 3:
                self.lst.pop(bisect.bisect_left(self.lst, (start, 1)))
                self.lst.pop(bisect.bisect_left(self.lst, (end, -1)))
                return False

        return True