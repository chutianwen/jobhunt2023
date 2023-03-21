"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque, defaultdict


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        # self.print(node)

        copy_root = Node(val=node.val)
        explored = defaultdict(Node)

        q = deque([(node)])
        explored[node] = copy_root
        while q:
            cur_node = q.popleft()

            for neighbor in cur_node.neighbors:
                if neighbor not in explored:
                    copy_node = Node(neighbor.val)
                    explored[neighbor] = copy_node
                    explored[cur_node].neighbors.append(copy_node)
                    q.append(neighbor)
                else:
                    explored[cur_node].neighbors.append(explored[neighbor])

        # self.print(copy_root)

        return copy_root

    def print(self, node):

        explored = set()

        def helper(root):
            if root in explored:
                return
            if root:
                print(root.val)
                explored.add(root)
                for neighbor in root.neighbors:
                    print(f'neighbor: {neighbor.val}')
                    helper(neighbor)

        helper(node)


class WrongSolution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        self.print(node)
        print('\n')
        explored = defaultdict(Node)

        q = deque([(node)])

        while q:
            cur_node = q.popleft()
            # This will actually get the wrong node
            explored[cur_node] = Node(cur_node.val)

            for neighbor in cur_node.neighbors:
                if neighbor not in explored:
                    copy_node = Node(neighbor.val)
                    explored[cur_node].neighbors.append(copy_node)
                    # Then copy_neighbor won't be read after next queue pop
                    q.append(neighbor)
                else:
                    explored[cur_node].neighbors.append(explored[neighbor])

        self.print(explored[node])

        return explored[node]
