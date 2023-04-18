# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """

        cleaned = set()
        # up, left, down, right
        direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def dfs(cur_pos, cur_dir_idx):

            robot.clean()
            cleaned.add(cur_pos)

            for idx in range(4):
                new_dir_idx = (cur_dir_idx + idx) % 4
                if idx != 0:
                    robot.turnLeft()
                new_pos = (cur_pos[0] + direction[new_dir_idx][0], cur_pos[1] + direction[new_dir_idx][1])
                if new_pos not in cleaned and robot.move():
                    dfs(new_pos, new_dir_idx)

            robot.turnLeft()
            self._back(robot)

        dfs((0, 0), 0)

    def _back(self, robot):
        robot.turnLeft()
        robot.turnLeft()
        robot.move()
        robot.turnLeft()
        robot.turnLeft()

