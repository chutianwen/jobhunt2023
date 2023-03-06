import threading
import time


class TokenBucket:
    def __init__(self, rate, capacity):
        '''
        :param rate:        Indicative QPS at rate level
        :param capacity:    Maximum capacity the limiter should allow
        '''
        assert rate > 0, 'rate needs to be > 0'
        self.rate = rate
        self.capacity = capacity
        self.token_amount = 0

        self.lock = threading.Lock()
        fill_token_thread = threading.Thread(target=self._fill_token)
        fill_token_thread.daemon = True
        fill_token_thread.start()

    def allow(self):
        with self.lock:
            print(f'Current token left: {self.token_amount}')
            if self.token_amount > 0:
                self.token_amount -= 1
                return True
            else:
                return False

    def _run(self):
        pass

    def _fill_token(self):
        '''
        Every 1/rate second, fill the token
        :return:
        '''
        while True:
            with self.lock:
                self.token_amount = min(self.token_amount + 1, self.capacity)
            time.sleep(1.0 / self.rate)


if __name__ == '__main__':
    token_bucket = TokenBucket(rate=5, capacity=10)
    for idx in range(20):
        time.sleep(0.4)
        print(f'allow for {idx}th request:{token_bucket.allow()}')
