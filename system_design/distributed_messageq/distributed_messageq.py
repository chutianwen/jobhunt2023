from system_design.distributed_messageq.consistent_hash import ConsistentHash
import hashlib


class DistributedMessageQueue:
    def __init__(self, nodes, queue_name):
        self.nodes = nodes
        self.queue_name = queue_name
        self.hasher = ConsistentHash(nodes)
        self.queues = {}

    def _get_node(self, key):
        return self.hasher.get_node(key)

    def _get_queue(self, node):
        if node not in self.queues:
            self.queues[node] = []
        return self.queues[node]

    def put(self, message):
        key = hashlib.sha256(str(message).encode('utf-8')).hexdigest()
        node = self._get_node(key)
        queue = self._get_queue(node)
        queue.append(message)

    def get(self):
        for node in self.nodes:
            queue = self._get_queue(node)
            if queue:
                return queue.pop(0)
        return None

# Mock requests
requests = [
    {'id': 1, 'method': 'POST', 'url': 'https://api.example.com/v1/users', 'body': {'username': 'alice'}},
    {'id': 2, 'method': 'GET', 'url': 'https://api.example.com/v1/users/123'},
    {'id': 3, 'method': 'PUT', 'url': 'https://api.example.com/v1/users/123', 'body': {'username': 'bob'}},
    {'id': 4, 'method': 'DELETE', 'url': 'https://api.example.com/v1/users/456'}
]

# Instantiate DistributedQueue
nodes = ['node1', 'node2', 'node3']
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
