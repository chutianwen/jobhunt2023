import hashlib
from bisect import bisect_left
from system_design.utils.node import *


class ConsistentHash:
    def __init__(self, nodes, replicas=3):
        self.replicas = replicas
        self.ring = {}
        self.node_to_replicas = {}
        for node in nodes:
            for idx in range(self._get_num_virtual_nodes(node)):
                virtual_node_id = f"{node.id}:{idx}"
                key = self._get_hash(virtual_node_id)
                self.ring[key] = (virtual_node_id, node.id)
        self.keys = sorted(self.ring.keys())

        # Handle replica nodes.
        for idx, key in enumerate(self.keys):
            primary_virtual_node, primary_node = self.ring[key]
            if primary_virtual_node not in self.node_to_replicas:
                self.node_to_replicas[primary_virtual_node] = []

            remaing_replica = self.replicas
            cur_idx = idx
            while remaing_replica > 0:
                # Clock wise pick replica nodes, given self.keys is sorted
                cur_idx += 1
                replica_node_idx = cur_idx % len(self.keys)
                replica_virtual_node, replica_node = self.ring[self.keys[replica_node_idx]]
                if replica_node == primary_node:
                    continue
                else:
                    self.node_to_replicas[primary_virtual_node].append(replica_virtual_node)
                    remaing_replica -= 1
        print(f'Number of keys: {len(self.keys)}')
        print(f'Hash Ring: {self.ring}')
        print(self.node_to_replicas)

    def _get_num_virtual_nodes(self, node: Node):
        size = node.size
        if size == LARGE_SIZE:
            return 5
        elif size == MEDIUM_SIZE:
            return 3
        elif size == SMALL_SIZE:
            return 1
        else:
            raise ValueError(f"Invalid size '{size}' for node '{node.id}'")

    def _get_hash(self, value):
        '''
        The 2^64 limit is the maximum value that can be represented by a 64-bit integer, which is a common data type
        used in computer systems. This limit is relevant in some contexts, such as when storing or manipulating integers
        or performing arithmetic operations on them.
        In the context of consistent hashing, the 2^64 limit is relevant in the sense that the range of values used in
        the hash function typically falls within this limit. This means that each node in the system is responsible for
        a range of values that is a subset of this range, and the total range of values is typically divided into a
        large number of small ranges to ensure that the distribution of keys is uniform.
        However, the specific hash function used in consistent hashing (such as hashlib.sha256) is not constrained by
        the maximum value of a 64-bit integer, as it generates a hash value that can be represented as a string with
        many more characters than 64. The important factor in choosing a hash function is that it generates a uniform
        distribution of hash values, regardless of the size of the range of values being used.
        '''
        # hashval = hashlib.sha256(f"{node}:{replica_index}".encode('utf-8')).hexdigest()
        hashval = hashlib.sha256(f"{value}".encode('utf-8')).hexdigest()
        return int(hashval, 16)

    def get_node(self, key):
        if not self.ring:
            return None
        hashval = self._get_hash(key)
        index = bisect_left(self.keys, hashval) % len(self.keys)
        return self.ring[self.keys[index]]
