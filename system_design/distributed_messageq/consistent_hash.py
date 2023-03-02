import hashlib
from bisect import bisect_left


class ConsistentHash:
    def __init__(self, nodes, replicas=3):
        self.replicas = replicas
        self.ring = {}
        for node in nodes:
            for i in range(replicas):
                key = self._get_key(node, i)
                self.ring[key] = node
        self.keys = sorted(self.ring.keys())

    def _get_key(self, node, replica_index):
        hashval = hashlib.sha256(f"{node}:{replica_index}".encode('utf-8')).hexdigest()
        return int(hashval, 16)

    def get_node(self, key):
        if not self.ring:
            return None
        hashval = hashlib.sha256(str(key).encode('utf-8')).hexdigest()
        key = int(hashval, 16)
        index = bisect_left(self.keys, key) % len(self.keys)
        return self.ring[self.keys[index]]
