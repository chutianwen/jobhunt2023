class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # binary search, x axis: shipping cap, y axis: days, mono decreasing, find the most left shipping cap.

        max_ship_cap = sum(weights)
        min_ship_cap = max(weights)

        while min_ship_cap <= max_ship_cap:
            mid_ship_cap = min_ship_cap + (max_ship_cap - min_ship_cap) // 2

            mid_cap_ship_days = self.get_num_ship_days(weights, mid_ship_cap)
            # print(f'mid_ship_cap:{mid_ship_cap}, mid_cap_ship_days:{mid_cap_ship_days}')
            # print(min_ship_cap, mid_ship_cap, max_ship_cap)
            if mid_cap_ship_days > days:
                min_ship_cap = mid_ship_cap + 1
            else:
                max_ship_cap = mid_ship_cap - 1

        return min_ship_cap

    def get_num_ship_days(self, weights, ship_cap):
        num_days = 0
        budget = 0
        for weight in weights:
            if budget >= weight:
                budget -= weight
            else:
                if budget < 0:
                    raise 'something wrong'
                num_days += 1
                budget = ship_cap - weight
        return num_days

