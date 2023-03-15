from collections import defaultdict
import heapq


class Solution:
    '''

    Each state, we need a representation as (loc, bus_id_taken_here), because from [+], you may take different buses to
    the neightbors, which has different cost. When marked as explored, we also need to add state only for "taken this bus
    to such location".
    In such problems, we cannot just think of nodes as stops like A, B, C. Even at the same location say B, it will take
    different cost to neighbor like C, depending an what bus is currently taking.
    For graph problems like this, the edge cost/distance is not static or fixed, it is a function of current node state
    and the edge property (which bus to take next).

    For building graph, one way is graph[src][dst] = set(path), another way is graph[src][path] = dst

          []- []
          \   \
    + -> [+] - []
    \     \
    + <-  +
    '''
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        graph = defaultdict(dict)
        for bus_idx, route in enumerate(routes):
            num_stops = len(route)
            if num_stops > 1:
                full_route = route + [route[0]]
                start_idx = 0
                while start_idx < num_stops:
                    graph[full_route[start_idx]][bus_idx] = full_route[start_idx + 1]
                    start_idx += 1

        # num_bus_taken, src, cur_bus_idx
        q = [(0, source, -1)]
        heapq.heapify(q)
        explored = set()
        while q:
            num_bus_taken, loc, cur_bus_idx = heapq.heappop(q)
            # print(num_bus_taken, loc, cur_bus_idx )

            if loc == target and num_bus_taken > 0:
                return num_bus_taken

            explored.add((loc, cur_bus_idx))

            for next_bus_idx, next_stop in graph.get(loc, {}).items():
                next_num_bus_taken = num_bus_taken

                if next_bus_idx != cur_bus_idx:
                    next_num_bus_taken += 1

                if (next_stop, next_bus_idx) not in explored:
                    heapq.heappush(q, (next_num_bus_taken, next_stop, next_bus_idx))
            # steps -= 1
        return -1