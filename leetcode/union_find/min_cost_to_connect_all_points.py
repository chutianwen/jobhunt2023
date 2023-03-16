import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        explored = set()
        graph = set()
        for x, y in points:
            graph.add((x, y))

        start = graph.pop()
        q = [(self._distance(start, node), start, node) for node in graph]
        heapq.heapify(q)
        # print(q)
        total_cost = 0
        explored.add(start)
        # print(start)
        while len(explored) <= len(graph):
            distance, src, dst = heapq.heappop(q)
            # print(f'src:{src}, dst:{dst}, distance:{distance}')
            if dst not in explored:
                explored.add(dst)
                total_cost += distance

                for next_dst in graph:
                    if next_dst not in explored:
                        heapq.heappush(q, (self._distance(dst, next_dst), dst, next_dst))

        return total_cost

    def _distance(self, u, v):
        return abs(u[0] - v[0]) + abs(u[1] - v[1])


# src:(0, 0), dst:(2, 2), distance:4
# src:(2, 2), dst:(5, 2), distance:3
# src:(5, 2), dst:(7, 0), distance:4
# src:(0, 0), dst:(5, 2), distance:7
# src:(0, 0), dst:(7, 0), distance:7
# src:(2, 2), dst:(7, 0), distance:7
# src:(2, 2), dst:(3, 10), distance:9
#
#
#
# src:(0, 0), dst:(2, 2), distance:4
# src:(2, 2), dst:(5, 2), distance:3
# src:(5, 2), dst:(7, 0), distance:4
# src:(7, 0), dst:(3, 10), distance:14