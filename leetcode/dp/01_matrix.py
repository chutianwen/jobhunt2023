class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return [[]]

        num_rows = len(mat)
        num_cols = len(mat[0])

        distance_matric = [[-1 for _ in range(num_cols)] for _ in range(num_rows)]

        # up, down, left, right
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        # traverse to get the first tier of 0
        frontier = []
        for row in range(num_rows):
            for col in range(num_cols):
                if mat[row][col] == 0:
                    distance_matric[row][col] = 0
                    frontier.append((row, col))

        while frontier:
            next_frontier = []

            for row, col in frontier:
                for row_change, col_change in directions:
                    next_row = row + row_change
                    next_col = col + col_change
                    if 0 <= next_row < num_rows and 0 <= next_col < num_cols:
                        if distance_matric[next_row][next_col] == -1:
                            distance_matric[next_row][next_col] = distance_matric[row][col] + 1
                            next_frontier.append((next_row, next_col))

            frontier = next_frontier

        return distance_matric
