import time


class FixedWindowCounter:

    def __init__(self, window, rate):
        '''

        :param window:  Every {window} seconds is a block
        :param rate:    Allow up to [rate} requests per window
        '''
        self.window = window
        self.rate = rate

        self.start_time_seconds = int(time.time())
        self.pre_window_idx = 0 // self.window
        self.cur_allowance = self.rate
        self._run()

    def _run(self):
        while True:
            msg = input('Type anything as a request>')
            self.allow()

    def allow(self):
        cur_time_seconds = int(time.time())
        # print(cur_time_seconds, self.start_time_seconds)
        cur_window_idx = (cur_time_seconds - self.start_time_seconds) // self.window
        print(f'pre_window_idx:{self.pre_window_idx}, cur_window_idx:{cur_window_idx}, cur_allowance:{self.cur_allowance}')
        if cur_window_idx == self.pre_window_idx:
            if self.cur_allowance > 0:
                self.cur_allowance -= 1
                return True
            else:
                return False
        else:
            self.cur_allowance = self.rate - 1
            self.pre_window_idx = cur_window_idx
            return True


if __name__ == '__main__':
    fixed_window_counter = FixedWindowCounter(window=1, rate=5)

    # for idx in range(20):
    #     time.sleep(2)
    #     print(f'{idx}th request is allowed:{fixed_window_counter.allow()}')
