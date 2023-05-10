from collections import defaultdict


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(defaultdict)

        for equation, value in zip(equations, values):
            parent, child = equation
            graph[parent][child] = value
            graph[child][parent] = 1 / value

        answers = []
        # print(graph)
        for src, dst in queries:
            if src not in graph or dst not in graph:
                answers.append(-1)
                continue

            stack = [(src, 1)]
            explored = set()
            is_added = False
            while stack:
                cur_node, cur_value = stack.pop()
                if cur_node == dst:
                    answers.append(cur_value)
                    is_added = True
                    break
                explored.add(cur_node)
                for next_node, fold in graph[cur_node].items():
                    if next_node not in explored:
                        stack.append((next_node, cur_value * fold))

            if not is_added:
                answers.append(-1)

        return answers




