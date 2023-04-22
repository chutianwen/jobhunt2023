from collections import Counter, defaultdict

from collections import defaultdict, Counter


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
