from collections import defaultdict


class Node:
    def __init__(self):
        self.parent = self
        self.size = 1

    def find(self):
        if self.parent != self:
            return self.parent.find()
        else:
            return self

    def union(self, target):
        self_parent, target_parent = self.find(), target.find()
        if self_parent == target_parent:
            return False

        if self_parent.size <= target_parent.size:
            self_parent.parent = target_parent
            if self_parent.size == target_parent.size:
                target_parent.size += 1
        else:
            target_parent.parent = self_parent
        return True


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:

        num_island = []

        cur_num_island = 0

        neighbor_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        graph = defaultdict(Node)

        for row, col in positions:
            if (row, col) not in graph:

                graph[(row, col)] = Node()
                cur_num_island += 1

                for row_change, col_change in neighbor_directions:
                    neighbor_row, neighbor_col = row + row_change, col + col_change
                    if (neighbor_row, neighbor_col) in graph:
                        if graph[(neighbor_row, neighbor_col)].union(graph[(row, col)]):
                            cur_num_island -= 1

            num_island.append(cur_num_island)

        return num_island