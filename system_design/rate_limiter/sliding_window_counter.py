import time


class SlidingWindowCounter:
    def __init__(self, window, rate):
        self.window = window
        self.rate = rate

        self.start_time_seconds = int(time.time())
        self.pre_window_idx = 0
        self.left_window_amount = 0
        self.cur_window_amount = 0

        print(f'Initial start_time_seconds:{self.start_time_seconds}')
        self._run()

    def _run(self):
        while True:
            msg = input('Type anything as a request>')
            self.allow()

    def allow(self):
        cur_time_stamp = time.time()
        cur_time_seconds = int(cur_time_stamp)
        cur_window_idx = (cur_time_seconds - self.start_time_seconds) // self.window

        print(f'cur_time_stamp:{cur_time_stamp}')
        print(f'cur_time_seconds:{cur_time_seconds}')

        print(f'pre_window_idx:{self.pre_window_idx}')
        print(f'cur_window_idx:{cur_window_idx}')

        print(f'left_window_amount:{self.left_window_amount}')
        print(f'cur_window_amount:{self.cur_window_amount}')

        if cur_window_idx == self.pre_window_idx:
            self.cur_window_amount += 1
        elif cur_window_idx == self.pre_window_idx + 1:
            self.left_window_amount = self.cur_window_amount
            self.cur_window_amount = 1
        else:
            self.left_window_amount = 0
            self.cur_window_amount = 1

        self.pre_window_idx = cur_window_idx

        last_window_amount = self.cur_window_amount + self.left_window_amount * (self.window - cur_time_stamp + cur_time_seconds) / self.window
        print(f'sliding window amount:{last_window_amount}')
        if last_window_amount <= self.rate:
            return True
        else:
            return False


if __name__ == '__main__':
    sliding_window_counter = SlidingWindowCounter(window=1, rate=5)