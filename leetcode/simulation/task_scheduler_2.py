from collections import defaultdict


class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:

        # task: step_idx insert
        task_last_insert_map = defaultdict(int)

        # pointer for tasks list
        task_id = 0

        # record number of steps
        step_id = 0

        while task_id <= len(tasks) - 1:

            cur_task_id = tasks[task_id]
            # never process this type yet, directly process it and record its last time
            if cur_task_id not in task_last_insert_map:
                task_last_insert_map[cur_task_id] = step_id
            else:
                task_last_insert_step = task_last_insert_map[cur_task_id]
                step_diff = step_id - task_last_insert_step
                # given n = 2, <2, 0> => 2 is not valid, need to be 3 at least 2 in between
                if step_diff <= space:
                    step_id += (space - step_diff + 1)

                task_last_insert_map[cur_task_id] = step_id

            step_id += 1
            task_id += 1

        return step_id






