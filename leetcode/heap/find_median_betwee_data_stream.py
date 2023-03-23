import heapq


class MedianFinder:

    def __init__(self):
        # max_heap tracks the left half, value inside needs to *-1
        self.max_heap = []
        self.size_max_heap = 0

        # min_heap tracks the right half
        self.min_heap = []
        self.size_min_heap = 0

        # need to keep balance the heap to make sure size_max_heap <= size_min_heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, num * -1)
        heapq.heappush(self.min_heap, heapq.heappop(self.max_heap) * -1)
        self.size_min_heap += 1
        if self.size_max_heap < self.size_min_heap - 1:
            heapq.heappush(self.max_heap, heapq.heappop(self.min_heap) * -1)
            self.size_min_heap -= 1
            self.size_max_heap += 1

    def addNum2(self, num: int) -> None:
        '''
        Make sure min_heap (right) is always equal or 1 size larger than the left.
        '''
        if self.size_min_heap == 0 or num <= heapq.nsmallest(1, self.min_heap)[0]:
            heapq.heappush(self.max_heap, num * -1)
            self.size_max_heap += 1
        else:
            heapq.heappush(self.min_heap, num)
            self.size_min_heap += 1

        # balance two heap size, if left size is too small
        while self.size_max_heap < self.size_min_heap - 1:
            value_from_right = heapq.heappop(self.min_heap)
            self.size_min_heap -= 1
            heapq.heappush(self.max_heap, value_from_right * -1)
            self.size_max_heap += 1

        # balance two heap size, if left size is too large
        while self.size_max_heap > self.size_min_heap:
            value_from_left = heapq.heappop(self.max_heap) * -1
            self.size_max_heap -= 1
            heapq.heappush(self.min_heap, value_from_left)
            self.size_min_heap += 1

    def addNum3(self, num: int) -> None:
        # add to max_heap left half first, and check if size of two heaps are balanced,
        heapq.heappush(self.max_heap, -1 * num)
        self.size_max_heap += 1

        while self.size_max_heap > self.size_min_heap:
            value_from_left = -1 * heapq.heappop(self.max_heap)
            self.size_max_heap -= 1
            heapq.heappush(self.min_heap, value_from_left)
            self.size_min_heap += 1

        while self.size_max_heap > 0 and heapq.nsmallest(1, self.max_heap)[0] * -1 > heapq.nsmallest(1, self.min_heap)[
            0]:
            value_from_left = -1 * heapq.heappop(self.max_heap)
            value_from_right = heapq.heappop(self.min_heap)
            heapq.heappush(self.min_heap, value_from_left)
            heapq.heappush(self.max_heap, value_from_right * -1)

    def findMedian(self) -> float:
        value_from_right = self.min_heap[0]

        if self.size_max_heap > 0 and self.size_max_heap == self.size_min_heap:
            median = (self.max_heap[0] * -1 + value_from_right) / 2
            return median
        else:
            return value_from_right

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()