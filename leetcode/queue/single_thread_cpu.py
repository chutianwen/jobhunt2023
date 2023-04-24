import heapq


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        if not tasks:
            return []

        task_with_ids = []
        for task_id, task in enumerate(tasks):
            task_start, task_duration = task
            task_with_ids.append((task_start, task_duration, task_id))

        sorted_tasks = sorted(task_with_ids)

        q = []
        task_order = []
        global_time = 0
        global_idx = 0

        while len(task_order) < len(tasks):
            if len(q) == 0:
                next_task_start, next_task_duration, next_task_id = sorted_tasks[global_idx]
                global_idx += 1
                global_time = next_task_start
                heapq.heappush(q, (next_task_duration, next_task_id, next_task_start))
            else:
                cur_task_duration, cur_task_id, cur_task_start = heapq.heappop(q)
                global_time += cur_task_duration

                task_order.append(cur_task_id)

                # check children
                while global_idx <= len(sorted_tasks) - 1:
                    next_task_start, next_task_duration, next_task_id = sorted_tasks[global_idx]
                    if next_task_start <= global_time:
                        heapq.heappush(q, (next_task_duration, next_task_id, next_task_start))
                        global_idx += 1
                    else:
                        break

        return task_order