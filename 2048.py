"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def merge(line):
    """
    Helper function that merges a single row or column in 2048

    line is a input int array and return the correct int array after merging
    """
    if (len(line) < 2):  # return 0 or 1 item list
        return line

    zero_loc = 0  # to find number 0 location
    new_line = []  # to pass the list to a new list
    while (zero_loc != len(line)):
        if (line[zero_loc] != 0):
            new_line.append(line[zero_loc])

        zero_loc += 1

    index = 0
    while (index < len(new_line) - 1):  # index < last 1 index
        if (new_line[index + 1] == new_line[index]):
            new_line[index] += new_line[index + 1]
            new_line.pop(index + 1)

        index += 1

    while (len(new_line) < len(line)):
        new_line.append(0)

    return new_line


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self.height = grid_height
        self.width = grid_width
        self.grid = [[0 for dummy_x in xrange(self.width)] for dummy_y in xrange(self.height)]
        self.initial = {UP: [(0, dummy_x) for dummy_x in xrange(self.width)],
                        DOWN: [(self.height - 1, dummy_x) for dummy_x in xrange(self.width)],
                        LEFT: [(dummy_x, 0) for dummy_x in xrange(self.height)],
                        RIGHT: [(dummy_x, self.width - 1) for dummy_x in xrange(self.height)]}

    def reset(self):
        """
        Reset the game so the grid is empty.
        """
        # replace with your code
        self.grid = [[0 for dummy_x in xrange(self.width)] for dummy_y in xrange(self.height)]

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        return str(self.grid)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self.height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self.width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        bool_move = False

        for dummy_cord in self.initial[direction]:
            line = [dummy_cord]
            # print line
            temp_loc = dummy_cord
            if (direction == UP or direction == DOWN):
                for dummy_add in range(self.height - 1):
                    temp_loc = (temp_loc[0] + OFFSETS[direction][0], temp_loc[1] + OFFSETS[direction][1])
                    line.append(temp_loc)
            else:
                for dummy_add in range(self.width - 1):
                    temp_loc = (temp_loc[0] + OFFSETS[direction][0], temp_loc[1] + OFFSETS[direction][1])
                    line.append(temp_loc)
            # print line
            values = []
            for dummy_each in line:
                values.append(self.grid[dummy_each[0]][dummy_each[1]])
            new_values = merge(values)
            if (values != new_values):
                bool_move = True

            index = 0
            for dummy_each in line:
                self.grid[dummy_each[0]][dummy_each[1]] = new_values[index]
                index += 1
                # print values
        if (bool_move):
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        height = random.randrange(self.height)
        width = random.randrange(self.width)

        while (self.grid[height][width] != 0):
            height = random.randrange(self.height)
            width = random.randrange(self.width)

        if (random.randrange(10) == 0):
            self.grid[height][width] = 4
        else:
            self.grid[height][width] = 2

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self.grid[row][col]


# import user34_LwMGqdaMGP_9 as poc_2048_tests
# poc_2048_tests.run_tests(TwentyFortyEight)

poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
