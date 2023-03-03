from system_design.utils.consistent_hash import ConsistentHash
from system_design.utils.node import *
from collections import defaultdict, Counter
import random


class ShardedCounter:

    def __init__(self, nodes):
        '''
        :param nodes: Number of shards
        '''
        self.consistent_hash = ConsistentHash(nodes)
        # from node_id to a local counter
        self.shard_counters = defaultdict(Counter)

    def incr(self, key, amount=1):
        '''
        Each time we will add some random part to the key, so it can hashed into a different
        shard/partition handled by a different node
        '''
        updated_key = f'{key}:{random.random()}'
        virtual_node, node = self.consistent_hash.get_node(updated_key)
        shard_counter = self.shard_counters[virtual_node]
        shard_counter[key] += amount

    def get(self, key):
        print(self.shard_counters)
        count = 0
        for node in self.shard_counters:
            count += self.shard_counters[node][key]
        return count


if __name__ == '__main__':
    nodes = [
        Node('node1', SMALL_SIZE),
        Node('node2', SMALL_SIZE),
        Node('node3', SMALL_SIZE)]

    counter = ShardedCounter(nodes=nodes)

    # increment some counts
    counter.incr('apple')
    counter.incr('banana', 2)
    counter.incr('cherry')
    counter.incr('banana')
    counter.incr('apple', 3)
    counter.incr('apple', 10)
    counter.incr('apple', 25)

    # get the counts for some keys
    print(counter.get('apple'))  # should print 4
    print(counter.get('banana'))  # should print 3
    print(counter.get('cherry'))  # should print 1
    print(counter.get('durian'))  # should print 0