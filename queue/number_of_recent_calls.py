class RecentCounter:

    def __init__(self):
        self.data = {}
        self.pre = None

    def ping(self, t: int) -> int:
        bucket = t % 3001
        if self.pre and self.pre == t:
            cnt, time = self.data[bucket]
            self.data[bucket] = (cnt + 1, t)
        else:
            self.data[bucket] = (1, t)

        res = 0
        keys_remove = set()
        for bucket in self.data:
            cnt, time = self.data[bucket]
            if time + 3000 >= t:
                res += cnt
            else:
                keys_remove.add(bucket)
        22, 414.48
        for key in keys_remove:
            self.data.pop(key)
        self.pre = t
        return res

    # Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

from collections import deque


class RecentCounter2:

    def __init__(self):
        self.data = deque([])

    def ping(self, t: int) -> int:
        self.data.append(t)
        while self.data[0] + 3000 < t:
            self.data.popleft()

        return len(self.data)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
