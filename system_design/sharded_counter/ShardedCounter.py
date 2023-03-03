from collections import defaultdict, Counter
from system_design.utils.consistent_hash import ConsistentHash
from system_design.utils.node import *
from threading import Thread
import random


class ShardedCounter:

    def __init__(self, nodes):
        '''
        :param nodes: Number of shards
        '''
        self.consistent_hash = ConsistentHash(nodes)
        # from node_id to a local counter
        # Since python defaultdict and Counter type are thread-safe, so we don't need to
        # create locks to handle concurrently writes (incr)
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


def test_single_user(counter):
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


def test_concurrent_users(sharded_counter):

    def process_request(sharded_counter, key):
        '''
        Simulate a user making a request to increment the counter for the given key
        '''
        sharded_counter.incr(key, 1)

    # Create 5 threads that increment the counter for the same key
    threads = []
    for i in range(100000):
        thread = Thread(target=process_request, args=(sharded_counter, 'apple'))
        threads.append(thread)

    # Start all the threads
    for thread in threads:
        thread.start()

    # Wait for all the threads to finish
    for thread in threads:
        thread.join()

    # Print the final count for the key
    print(sharded_counter.get('apple'))


if __name__ == '__main__':
    nodes = [
        Node('node1', SMALL_SIZE),
        Node('node2', SMALL_SIZE),
        Node('node3', SMALL_SIZE)]

    counter = ShardedCounter(nodes=nodes)

    # test_single_user(counter)

    test_concurrent_users(counter)