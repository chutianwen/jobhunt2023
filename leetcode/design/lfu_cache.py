from collections import defaultdict, OrderedDict


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = None
        self.key_value_map = defaultdict(int)
        self.key_freq_map = defaultdict(int)
        # value is any placeholder
        self.freq_key_map = defaultdict(OrderedDict)

    def get(self, key: int) -> int:
        if key not in self.key_value_map:
            return -1
        else:
            self._update_freq(key)
            # print(f'get key:{key}')
            # self._debug()
            return self.key_value_map[key]

    def put(self, key: int, value: int) -> None:
        # print(f'put key:{key}, value:{value}')
        # Note that no need to trim when key is inside the map
        if key not in self.key_value_map and len(self.key_value_map) == self.capacity:
            min_freq_keys = self.freq_key_map[self.min_freq]
            oldest_key, _ = min_freq_keys.popitem(last=False)
            self.key_freq_map.pop(oldest_key)
            self.key_value_map.pop(oldest_key)
            if not min_freq_keys:
                self.freq_key_map.pop(self.min_freq)
            self.min_freq = min(self.freq_key_map.keys()) if self.freq_key_map else None

        self.key_value_map[key] = value
        if key not in self.key_freq_map:
            self.key_freq_map[key] = 1
            self.min_freq = 1
            self.freq_key_map[1][key] = ''
        else:
            self._update_freq(key)
        # self._debug()

    def _update_freq(self, key):
        if key in self.key_freq_map:
            cur_freq = self.key_freq_map.pop(key)
            next_freq = cur_freq + 1
            self.key_freq_map[key] = next_freq

            self.freq_key_map[cur_freq].pop(key)
            self.freq_key_map[next_freq][key] = ''

            # remove freq key
            if not self.freq_key_map[cur_freq]:
                self.freq_key_map.pop(cur_freq)
                if self.min_freq == cur_freq:
                    self.min_freq = next_freq

    def _debug(self):
        print(f'key_freq_map:{self.key_freq_map}')
        print(f'freq_key_map:{self.freq_key_map}')
        print(f'self min:{self.min_freq}')

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)