from bisect import bisect_left

class HitCounter:
    def __init__(self, last_n_second):
        self.last_n_second = last_n_second
        self.q = []

    def read(self, mocked_time):
        self._trim_old_cnt(mocked_time)

        if not self.q or self.q[-1][0] != mocked_time:
            self.q.append((mocked_time, 1))
        else:
            self.q[-1][1] += 1

    def _trim_old_cnt(self, base_time):
        cut_off_time = base_time - self.last_n_second
        cut_off_idx = bisect_left(self.q, (cut_off_time, 1e10))
        self.q = self.q[cut_off_idx:]

    def read_load_stats(self, mocked_time):
        self._trim_old_cnt(mocked_time)
        total_cnt = 0
        for timestamp, cnt in self.q:
            if timestamp <= mocked_time:
                total_cnt += cnt

        return total_cnt


hit_counter = HitCounter(last_n_second=60)

for t in range(80):
    hit_counter.read(t)
    read_stats = hit_counter.read_load_stats(t)
    print(f'At time:{t}, read_stats is:{read_stats}')