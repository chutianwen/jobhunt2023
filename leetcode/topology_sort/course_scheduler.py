from collections import defaultdict

from collections import defaultdict, deque

from collections import defaultdict, deque


class TopDownFrontierTrimSolution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # build a graph
        graph = defaultdict(set)
        node_parent_map = defaultdict(set)

        for child, parent in prerequisites:
            graph[parent].add(child)
            node_parent_map[child].add(parent)

        # from top down trimming
        q = deque([node for node in range(numCourses) if node not in node_parent_map])

        course_order = []

        while q:
            course_order.extend(q)
            new_q = []
            for cur_node in q:
                for next_node in graph.get(cur_node, []):
                    node_parent_map[next_node].remove(cur_node)
                    if len(node_parent_map[next_node]) == 0:
                        new_q.append(next_node)
                        node_parent_map.pop(next_node)
            q = new_q

        if len(course_order) == numCourses:
            return course_order
        else:
            return



class TopDownSolution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # build a graph
        graph = defaultdict(set)
        node_parent_map = defaultdict(set)
        for course_idx in range(numCourses):
            graph[course_idx]

        for child, parent in prerequisites:
            graph[parent].add(child)
            node_parent_map[child].add(parent)

        # from top down trimming
        q = deque([node for node in graph if node not in node_parent_map])

        course_order = []

        while q:
            cur_node = q.popleft()
            course_order.append(cur_node)

            for next_node in graph.get(cur_node, []):
                node_parent_map[next_node].remove(cur_node)
                if len(node_parent_map[next_node]) == 0:
                    q.append(next_node)
                    node_parent_map.pop(next_node)

        if len(course_order) == numCourses:
            return course_order
        else:
            return []


from collections import defaultdict, deque


class BotUpSolution2:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # build a graph
        graph = defaultdict(set)
        node_parent_map = defaultdict(set)
        for child, parent in prerequisites:
            graph[parent].add(child)
            node_parent_map[child].add(parent)

        # from bot up, leaves
        q = deque([node for node in range(numCourses) if node not in graph])

        course_order = []

        while q:
            node = q.popleft()
            course_order.insert(0, node)

            for parent in node_parent_map.get(node, set()):
                graph[parent].remove(node)
                if len(graph[parent]) == 0:
                    q.append(parent)

        if len(course_order) == numCourses:
            return course_order
        else:
            return



class BotUpSolution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # build a graph
        graph = defaultdict(list)
        for course_idx in range(numCourses):
            graph[course_idx]

        for child, parent in prerequisites:
            graph[parent].append(child)

        # traverse the node within graph, update the order

        explored = set()
        course_order = []

        def traverse_has_circle(node, path_explored):
            # print(node, path_explored, explored)
            if node in path_explored:
                return True

            if node in explored:
                return False

            path_explored.add(node)
            for next_node in graph.get(node, []):
                if traverse_has_circle(next_node, path_explored):
                    return True

            path_explored.remove(node)

            course_order.insert(0, node)
            explored.add(node)
            return False

        print(graph)
        for node in graph:

            if traverse_has_circle(node, set()):
                return []

        return course_order if len(explored) == numCourses else []