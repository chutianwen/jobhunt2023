from collections import defaultdict, deque


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]
        graph = defaultdict(set)
        for src, dst in edges:
            graph[src].add(dst)
            graph[dst].add(src)

        q = deque([(node, 0) for node in graph if len(graph[node]) == 1])

        res = []
        visited = 0
        while q:
            # print(q)
            cur_node, depth = q.popleft()
            visited += 1
            if depth == len(res):
                res.append([])

            res[depth].append(cur_node)

            if graph[cur_node]:
                parent = graph[cur_node].pop()
                graph[parent].remove(cur_node)
                if len(graph[parent]) == 1:
                    q.append((parent, depth + 1))

            graph.pop(cur_node)

        # print(res)
        if visited != n: raise Exception("circle detected")
        return res[-1]