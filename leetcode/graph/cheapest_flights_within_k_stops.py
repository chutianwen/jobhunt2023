import heapq
from collections import defaultdict


class Solution:
    '''
    Here is finding shortest path with a condition on path capping.
    So we need to consider the less optimal path with shorter jumps.
    So model the state by only location is not enough, we should consider adding more fields to the
    state like number of jumps so far.
    '''
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        # total_price, total_stops, location
        q = [(0, 0, src)]
        heapq.heapify(q)

        graph = defaultdict(set)
        # this may conflict local variable src, better usign other names
        for s, d, price in flights:
            graph[s].add((price, d))

        explored = defaultdict(int)
        while q:
            # print(q)
            cur_price, cur_jumps, cur = heapq.heappop(q)

            # print(cur_price, cur_jumps, cur )
            explored[(cur, cur_jumps)] = cur_price

            if cur == dst and cur_jumps > 0:
                return cur_price

            total_jumps = cur_jumps + 1
            for next_price, next_dst in graph[cur]:
                total_price = cur_price + next_price

                if (next_dst, total_jumps) not in explored or total_price < explored[(next_dst, total_jumps)]:
                    if total_jumps <= k + 1:
                        # This can add extra unwanted time and space O, since (next_dst, total_jumps) may not be the best
                        # from the previous frontier, but they still added to the heap.
                        heapq.heappush(q, (total_price, total_jumps, next_dst))

        return -1

import string
string.ascii_lowercase
class SolutionFrontier:
    def findCheapestPrice(self, n, flights, src, dst, K):

class Solution2:
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        # build graph:
        from collections import defaultdict
        graph = defaultdict(dict)
        for src_t, des, cost in flights:
            graph[src_t][des] = cost

        # cheapest search
        best = {}
        frontier = [(0, 0, src)]
        import heapq
        limit = float('inf')
        while frontier:
            cost, stops, expand = heapq.heappop(frontier)
            if stops - 2 >= K or cost > best.get((stops, expand), limit):
                continue

            if expand == dst:
                return cost

            for dst_t, cost_next in graph[expand].items():
                cost_future = cost + cost_next
                if cost_future < best.get((stops + 1, dst_t), limit):
                    best[(stops + 1, dst_t)] = cost_future
                    heapq.heappush(frontier, (cost_future, stops + 1, dst_t))

        return -1