from collections import defaultdict


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        if not board or not board[0]:
            return False

        # up, down, left, right
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        row_bound = len(board)
        col_bound = len(board[0])
        word_length = len(word)
        explored = set()

        def find(idx, cur_row, cur_col):
            if idx == word_length:
                return True
            if not (0 <= cur_row < row_bound and 0 <= cur_col < col_bound):
                return False
            if (cur_row, cur_col) in explored:
                return False
            if word[idx] != board[cur_row][cur_col]:
                return False

            explored.add((cur_row, cur_col))

            for row_change, col_change in directions:
                next_row = cur_row + row_change
                next_col = cur_col + col_change

                if find(idx + 1, next_row, next_col):
                    return True

            explored.remove((cur_row, cur_col))
            return False

        for row in range(row_bound):
            for col in range(col_bound):
                if find(0, row, col):
                    return True

        return False


