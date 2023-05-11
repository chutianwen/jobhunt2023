import heapq
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        task_heap = [(-cnt, task) for task, cnt in Counter(tasks).items()]
        heapq.heapify(task_heap)

        tasks = []
        total_step = 0

        cycle_cnt = n + 1

        while task_heap:

            buffer = []
            cnt_task = 0

            while task_heap and cnt_task < cycle_cnt:
                task_cnt, task = heapq.heappop(task_heap)
                task_cnt *= -1

                tasks.append(task)

                task_cnt -= 1
                if task_cnt > 0:
                    buffer.append((-task_cnt, task))

                cnt_task += 1

            if buffer:
                tasks.extend(['idle'] * (cycle_cnt - cnt_task))
                total_step += cycle_cnt
                for cnt_task in buffer:
                    heapq.heappush(task_heap, cnt_task)
            else:
                total_step += cnt_task

        # print(tasks)
        return total_step


