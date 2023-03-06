import threading
import time


class LeakingBucket:

    def __init__(self, leak_rate, capacity):
        '''

        :param leak_rate:  Leak {leak_rate} per second
        :param capacity:
        '''
        self.leak_rate = leak_rate
        self.capacity = capacity

        self.lock = threading.Lock()
        self.cur_amount = 0

        leak_thread = threading.Thread(target=self._leak)
        leak_thread.daemon = True
        leak_thread.start()

        self._run()

    def _run(self):
        while True:
            msg = input('Type anything as a request>')
            print(f'inflow is succeed:{self.inflow()}')

    def inflow(self):
        with self.lock:
            print(f'Current amount:{self.cur_amount}')
            if self.cur_amount < self.capacity:
                self.cur_amount += 1
                return True
            else:
                print(f'Reaching capacity limit, drop!')
                return False

    def _leak(self):
        while True:
            with self.lock:
                self.cur_amount = max(self.cur_amount - self.leak_rate, 0)

            time.sleep(1)


if __name__ == '__main__':
    LeakingBucket(leak_rate=1, capacity=3)