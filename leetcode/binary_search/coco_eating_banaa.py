import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        lo = math.ceil(sum(piles) / h)
        hi = max(piles)

        while lo <= hi:
            mid = (lo + hi) // 2
            can_finish = self.can_finish(piles, mid, h)
            # print(lo, hi, can_finish)
            if can_finish:
                hi = mid - 1
            else:
                lo = mid + 1

        return lo

    def can_finish(self, piles, speed, h):
        budget = h
        for pile in piles:
            cost = math.ceil(pile / speed)
            budget -= cost
            if budget < 0:
                return False
        return True