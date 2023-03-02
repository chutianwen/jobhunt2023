import hashlib
from bisect import bisect_left


class ScaledConsistentHash:
    def __init__(self, nodes, replicas=3):
        self.replicas = replicas
        self.ring = {}
        self.keys = []
        for node in nodes:
            for i in range(replicas):
                key = self._get_key(node, i)
                self.ring[key] = node

            num_virtual_nodes = self._get_num_virtual_nodes(node)
            for i in range(num_virtual_nodes):
                key = self._get_key(node, i)
                self.ring[key] = node
                self.keys.append(key)
        self.keys.sort()

    def _get_key(self, node, replica_index):
        # Split node into virtual nodes based on its size
        num_virtual_nodes = self._get_num_virtual_nodes(node)
        virtual_nodes = [f"{node['name']}:{i}" for i in range(num_virtual_nodes)]

        # Generate hash value for each virtual node
        hashvals = [hashlib.sha256(virtual_node.encode('utf-8')).hexdigest() for virtual_node in virtual_nodes]
        keys = [int(hashval, 16) for hashval in hashvals]

        return keys[replica_index % num_virtual_nodes]

    def _get_num_virtual_nodes(self, node):
        # Determine the number of virtual nodes to assign to the node based on its size
        size = node.get('size', 'medium')
        if size == 'large':
            return 100
        elif size == 'medium':
            return 10
        elif size == 'small':
            return 1
        else:
            raise ValueError(f"Invalid size '{size}' for node '{node['name']}'")

    def get_node(self, key):
        if not self.ring:
            return None
        hashval = hashlib.sha256(str(key).encode('utf-8')).hexdigest()
        key = int(hashval, 16)
        index = bisect_left(self.keys, key) % len(self.keys)
        return self.ring[self.keys[index]]
