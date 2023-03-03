from system_design.utils.consistent_hash import ConsistentHash
from system_design.utils.node import *
import random

class DistributedMessageQueue:
    def __init__(self, nodes, queue_name):
        self.nodes = nodes
        self.queue_name = queue_name
        self.hasher = ConsistentHash(nodes)
        self.queues = {}

    def _get_queue(self, node):
        if node not in self.queues:
            self.queues[node] = []
        return self.queues[node]

    def put(self, message):
        virtual_node, node = self.hasher.get_node(message)
        queue = self._get_queue(virtual_node)
        queue.append(message)

    def get(self):
        random_nodes = list(self.queues.keys())
        random.shuffle(random_nodes)

        for node in random_nodes:
            queue = self.queues[node]
            if queue:
                return queue.pop(0)
        return None


if __name__ == '__main__':
    # Mock requests
    requests = [
        {'id': 1, 'method': 'POST', 'url': 'https://api.example.com/v1/users', 'body': {'username': 'alice'}},
        {'id': 2, 'method': 'GET', 'url': 'https://api.example.com/v1/users/123'},
        {'id': 3, 'method': 'PUT', 'url': 'https://api.example.com/v1/users/123', 'body': {'username': 'bob'}},
        {'id': 4, 'method': 'DELETE', 'url': 'https://api.example.com/v1/users/456'}
    ]

    # Instantiate DistributedQueue
    nodes = [
        Node('node1', LARGE_SIZE),
        Node('node2', MEDIUM_SIZE),
        Node('node3', SMALL_SIZE)]

    queue_name = 'requests'
    queue = DistributedMessageQueue(nodes, queue_name)

    # Enqueue requests
    for request in requests:
        queue.put(request)

    # Process requests
    while True:
        request = queue.get()
        if request is None:
            break
        # Process request
        print(f"Processing request {request['id']}: {request['method']} {request['url']} {request.get('body', '')}")
