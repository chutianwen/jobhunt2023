import heapq


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        if not trips:
            return True

        # maintain overlapping range and current overlapped cnt

        # sort based on the start
        trips.sort(key=lambda trip: trip[1])

        # (expiration, value)
        heap = []

        cnt = 0
        for num_passenger, left, right in trips:

            if not heap:
                heap.append((right, num_passenger))
                cnt += num_passenger
            else:
                while heap and heap[0][0] <= left:
                    _, value = heapq.heappop(heap)
                    cnt -= value

                heapq.heappush(heap, (right, num_passenger))
                cnt += num_passenger

            if cnt > capacity:
                return False

        return True
