import heapq


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks_with_id = [(start, duration, task_id) for task_id, (start, duration) in enumerate(tasks)]
        # sort based on start
        tasks_with_id.sort(key=lambda entry: (entry[0], entry[1]))

        buffer = []
        processed_tasks = []

        task_pointer = 0
        time = 0
        # print(f'tasks_with_id:{tasks_with_id}')

        while len(processed_tasks) < len(tasks):
            if not buffer:
                start, duration, task_id = tasks_with_id[task_pointer]
                time = start + duration
                task_pointer += 1
            else:
                duration, task_id = heapq.heappop(buffer)
                time += duration

            processed_tasks.append(task_id)
            while task_pointer <= len(tasks_with_id) - 1:
                next_start, next_duration, next_task_id = tasks_with_id[task_pointer]
                if next_start <= time:
                    heapq.heappush(buffer, (next_duration, next_task_id))
                    task_pointer += 1
                else:
                    break

        return processed_tasks

