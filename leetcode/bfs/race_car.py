from collections import deque


class Solution:

    def racecar(self, target: int) -> int:
        if target == 0:
            return 0

        # step, location, speed
        q = deque([(0, 0, 1)])

        # (loc, speed)
        explored = set()

        while q:
            # print(q)
            num_instructions, cur_loc, cur_speed = q.popleft()

            if cur_loc == target and num_instructions > 0:
                return num_instructions

            explored.add((cur_loc, cur_speed))

            # consider A:
            next_loc = cur_loc + cur_speed
            next_speed = cur_speed * 2
            if 0 < next_loc < 2 * target:
                if (next_loc, next_speed) not in explored:
                    q.append((num_instructions + 1, next_loc, next_speed))

            # consider R only if away from target:
            if (next_loc > target and cur_speed > 0) or (next_loc < target and cur_speed < 0):
                next_loc = cur_loc
                next_speed = -1 if cur_speed > 0 else 1
                if (cur_loc, next_speed) not in explored:
                    q.append((num_instructions + 1, next_loc, next_speed))
