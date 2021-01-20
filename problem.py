class Problem:
    def __init__(self, start, end, limit, grid, size):
        self.start = start  # start point
        self.end = end  # end point
        self.grid = grid  # the grid with the cost of all the nodes
        self.limit = limit  # the requsted limit of the problem
        self.size = size  # the size of the grid

    """
    The function checks if we reached the goal (end point)
    """

    def is_goal(self, node):
        return self.end == node.get_pos()

    """
    The function returns the size of the gird
    """

    def get_size(self):
        return self.size

    """
    The function returns the grid
    """

    def get_grid(self):
        return self.grid

    """
    The funtion returns the start point
    """

    def get_start(self):
        return self.start

    """
    The function returns the end point (goal point)
    """

    def get_end(self):
        return self.end

    """
    The funciton return the limit of the problem
    """

    def get_limit(self):
        return self.limit

    """
    The function set a new limit for the problem
    """

    def set_limit(self, l):
        self.limit = l

    """
    The function sets a new grid to the problem
    """

    def set_grid(self, g):
        self.grid = g
