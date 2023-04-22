class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:

        # if surrond is a wall, then we can determine next direction, if not, keeps moving with current direction
        # up, left, down, right
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        row_limit = len(maze)
        col_limit = len(maze[0])

        def within_bound(row, col):
            return 0 <= row < row_limit and 0 <= col < col_limit

        explored = set()

        def next_stop(cur_pos, cur_dir):
            while within_bound(cur_pos[0] + cur_dir[0], cur_pos[1] + cur_dir[1]) and maze[cur_pos[0] + cur_dir[0]][
                cur_pos[1] + cur_dir[1]] != 1:
                cur_pos = [cur_pos[0] + cur_dir[0], cur_pos[1] + cur_dir[1]]

            return cur_pos

        def rolling(cur_pos):
            # print(cur_pos)
            if cur_pos == destination:
                return True

            explored.add((cur_pos[0], cur_pos[1]))
            # check neighbor:

            for direction in directions:
                next_pos = next_stop(cur_pos, direction)
                if (next_pos[0], next_pos[1]) not in explored:
                    if rolling(next_pos):
                        return True

            return False

        return rolling(start)

