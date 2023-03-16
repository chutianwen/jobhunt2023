from collections import defaultdict


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-10, -10)
        self.head.right = self.tail
        self.tail.left = self.head
        self.lookup = defaultdict(Node)

    def get(self, key: int) -> int:
        if key in self.lookup:
            node = self.lookup[key]
            self._delete(node)
            self._add(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        if key in self.lookup:
            new_node = self.lookup[key]
            new_node.value = value
            self._delete(new_node)
        else:
            new_node = Node(key, value)
            if len(self.lookup) == self.capacity:
                delete_node = self.lookup.pop(self.head.right.key)
                self._delete(delete_node)

        self._add(new_node)
        self.lookup[key] = new_node

    def _add(self, node):
        self.tail.left.right, node.left, node.right, self.tail.left = node, self.tail.left, self.tail, node

    def _delete(self, node):
        node.left.right, node.right.left = node.right, node.left

    def _debug(self):
        p = self.head
        a = ''
        while p:
            a = f'{a}->{p.value}'
            p = p.right
        print(a)
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)