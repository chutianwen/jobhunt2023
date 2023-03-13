from collections import defaultdict


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        connections = defaultdict(set)
        for v1, v2 in edges:
            connections[v1].add(v2)
            connections[v2].add(v1)

        def get_depth(root, edges):
            branches = edges[root]
            # no more edges connecting such root, indicates root is a leaf node
            if not branches:
                return 0

            max_depth = float('-inf')
            for branch in branches:
                edges[root].remove(branch)
                edges[branch].remove(root)
                depth = get_depth(branch, edges)
                max_depth = max(max_depth, depth)
                edges[branch].add(root)
                edges[root].add(branch)
            return max_depth + 1

        min_depth = None
        min_depth_root = []

        # print(connections)

        for start in connections.keys():
            depth = get_depth(start, connections)
            # print(start, depth)
            if min_depth is None:
                min_depth = depth

            if min_depth > depth:
                min_depth_root = [start]
                min_depth = depth
            elif min_depth == depth:
                min_depth_root.append(start)
            else:
                continue

        return min_depth_root


class Solution2:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        connections = defaultdict(set)
        for v1, v2 in edges:
            connections[v1].add(v2)
            connections[v2].add(v1)

        while len(connections) > 2:
            leaves = [leave for leave in connections if len(connections[leave]) == 1]

            for leave in leaves:
                parent = connections[leave].pop()
                connections[parent].remove(leave)
                connections.pop(leave)

        return list(connections.keys())


class Solution3:
    def findMinHeightTrees(self, n, edges):
        '''
        This is a variant of BFS, that updates the whole frontier line at each iteration.
        '''
        if n == 1:
            return [0]

        adj = [set() for _ in range(n)]
        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)

        leaves = [i for i in range(n) if len(adj[i]) == 1]

        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for i in leaves:
                j = adj[i].pop()
                adj[j].remove(i)
                if len(adj[j]) == 1:
                    newLeaves.append(j)
            leaves = newLeaves
        return leaves
