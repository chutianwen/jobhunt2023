from collections import Counter, defaultdict

from collections import defaultdict, Counter

from collections import deque, defaultdict, Counter


class TopDownSolution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:

        node_indegree_map = defaultdict(list)
        node_out_degree_map = defaultdict(list)
        for src, dst in edges:
            node_out_degree_map[src].append(dst)
            node_indegree_map[dst].append(src)

        # nodes with zero indegree, root nodes
        frontier = deque([node for node in range(len(colors)) if node not in node_indegree_map])

        # maintain a counter recording state calculating from root to current node
        node_color_value_map = defaultdict(Counter)

        explored = 0
        largest_color, largest_color_value = None, None

        while frontier:
            cur_node = frontier.popleft()
            node_color_value_map[cur_node][colors[cur_node]] += 1

            explored += 1
            is_leaf = True
            for next_node in node_out_degree_map.get(cur_node, []):
                for color, color_cnt in node_color_value_map.get(cur_node, Counter()).items():
                    node_color_value_map[next_node][color] = max(node_color_value_map[next_node][color], color_cnt)

                node_indegree_map[next_node].remove(cur_node)
                if len(node_indegree_map[next_node]) == 0:
                    frontier.append(next_node)
                is_leaf = False

            # print(cur_node, is_leaf, node_color_value_map[cur_node])

            if is_leaf:
                cur_largest_color, cur_largest_color_value = \
                node_color_value_map.get(cur_node, Counter()).most_common()[0]
                if largest_color_value is None or largest_color_value < cur_largest_color_value:
                    largest_color, largest_color_value = cur_largest_color, cur_largest_color_value

        if explored < len(colors):
            return -1
        else:
            return largest_color_value

        # from top to bottom, expand frontier of nodes having 0 indegree



class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:

        graph = defaultdict(list)
        in_degree = set()
        for src, dst in edges:
            graph[src].append(dst)
            in_degree.add(dst)

        # traverse each root with indgree 0, update a global dict, key: node, value: counter (storing each char largest color value)
        root_nodes = [node_idx for node_idx in range(len(colors)) if node_idx not in in_degree]

        node_to_char_counter_map = defaultdict(Counter)

        def traverse(node, explored):
            if node in node_to_char_counter_map:
                return 0

            if node in explored:
                return -1

            explored.add(node)

            for next_node in graph.get(node, []):
                if traverse(next_node, explored) == -1:
                    return -1

            explored.remove(node)

            # update node_to_char_counter_map
            cur_counter = Counter()
            for next_node in graph.get(node, []):
                next_node_counter = node_to_char_counter_map.get(next_node, Counter())
                # print(next_node, next_node_counter)
                for color, color_count in next_node_counter.items():
                    cur_counter[color] = max(cur_counter[color], color_count)

            cur_counter[colors[node]] += 1
            node_to_char_counter_map[node] = cur_counter

            return 0

        largest_color, largest_color_value = None, None
        for root_node in root_nodes:
            explored = set()
            if traverse(root_node, explored) == -1:
                return -1
            else:
                # print(f'root_node:{root_node}, node_to_char_counter_map:{node_to_char_counter_map}')
                cur_largest_color, cur_largest_color_value = node_to_char_counter_map[root_node].most_common()[0]
                if largest_color_value is None or largest_color_value < cur_largest_color_value:
                    largest_color, largest_color_value = cur_largest_color, cur_largest_color_value

        if len(node_to_char_counter_map) == len(colors) and largest_color_value is not None:
            return largest_color_value
        else:
            return -1



class Solution2:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:

        # maintian a counter along the path, and traverse through each node in grpah as starting point

        # build graph
        graph = defaultdict(list)
        dsts = set()
        for src, dst in edges:
            graph[src].append(dst)
            dsts.add(dst)

        largest_color_value = 0
        # filter starting points from roots
        has_root = False
        for node in range(0, len(colors)):
            if node not in dsts:
                cur_color_value = self.traverse_color_value(node, graph, colors)
                if cur_color_value == -1:
                    return -1
                else:
                    largest_color_value = max(largest_color_value, cur_color_value)

                has_root = True

        if has_root is False:
            return -1

        return largest_color_value

    def traverse_color_value(self, node, graph, colors):
        counter = Counter()
        self.color_value = 0

        explored = set()

        def dfs(node):

            if node in explored:
                return -1

            counter[colors[node]] += 1
            explored.add(node)

            self.color_value = max(self.color_value, counter.most_common()[0][1])

            for next_node in graph.get(node, []):
                if dfs(next_node) == -1:
                    return -1

            counter[colors[node]] -= 1
            explored.remove(node)

            return self.color_value

        if dfs(node) == -1:
            return -1
        else:
            return self.color_value
