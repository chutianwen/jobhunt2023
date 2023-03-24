import bisect
import random


class Solution:

    def __init__(self, w: List[int]):
        self.accumulator = []
        cur = 0
        for number in w:
            cur += number
            self.accumulator.append(cur)

    def pickIndex(self) -> int:
        sample = random.uniform(0, self.accumulator[-1])
        idx = bisect.bisect_left(self.accumulator, sample)
        return idx
