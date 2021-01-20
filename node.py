class Node:
    def __init__(self, x, y, cost, depth, parent, direction):
        self.x = x  # x pos
        self.y = y  # y pos
        self.cost = cost  # the cost you pay to visit in the Node
        self.depth = depth  # the depth of the Node
        self.neighbors = []  # list of all the neighbors of the Node
        self.parent = parent  # the parent of the Node
        self.direction = direction  # which direction you go in order to get to that point

    """
    The function returns the position of the Node
    """

    def get_pos(self):
        return self.x, self.y

    """
    The function returns the parent of the Node
    the start point will have herself as a parent
    """

    def get_parent(self):
        return self.parent

    """
    The function returns the depth of the Node
    """

    def get_depth(self):
        return self.depth

    """
    The function returns the cost of the Node
    """

    def get_cost(self):
        return self.cost

    """
    The function updates the neighbors of the Node and returns the neighbors
    """
    # need to be fixed - maybe changed the cost to be -1 after visit

    def update_neighbors(self, problem):
        self.neighbors = []
        grid = problem.get_grid()
        size = problem.get_size()
        # RIGHT - R
        if self.y < size - 1 and grid[self.x][self.y + 1] != -1:
            self.neighbors.append(Node(
                self.x, self.y + 1, self.cost + grid[self.x][self.y + 1], self.depth + 1, self, 'R'))

        # RIGHT DIAGONAL DOWN - RD
        if self.y < size - 1 and self.x < size - 1 and (grid[self.x + 1][self.y] != -1 and grid[self.x][self.y + 1] != -1) and grid[self.x + 1][self.y + 1] != -1:
            self.neighbors.append(Node(
                self.x + 1, self.y + 1, self.cost + grid[self.x + 1][self.y + 1], self.depth + 1, self, "RD"))

        # DOWN - D
        if self.x < size - 1 and grid[self.x + 1][self.y] != -1:
            self.neighbors.append(Node(
                self.x + 1, self.y, self.cost + grid[self.x + 1][self.y], self.depth + 1, self, "D"))

        # LEFT DIAGONAL DOWN - LD
        if self.x < size - 1 and self.y > 0 and (grid[self.x + 1][self.y] != -1 and grid[self.x][self.y - 1] != -1) and grid[self.x + 1][self.y - 1] != -1:
            self.neighbors.append(Node(
                self.x + 1, self.y - 1, self.cost + grid[self.x + 1][self.y - 1], self.depth + 1, self, "LD"))

        # LEFT - L
        if self.y > 0 and grid[self.x][self.y - 1] != -1:
            self.neighbors.append(Node(
                self.x, self.y - 1, self.cost + grid[self.x][self.y - 1], self.depth + 1, self, "L"))

        # LEFT DIAGONAL UP - LU
        if self.y > 0 and self.x > 0 and (grid[self.x - 1][self.y] != -1 and grid[self.x][self.y - 1] != -1) and grid[self.x - 1][self.y - 1] != -1:
            self.neighbors.append(Node(
                self.x - 1, self.y - 1, self.cost + grid[self.x - 1][self.y - 1], self.depth + 1, self, "LU"))

        # UP - U
        if self.x > 0 and grid[self.x - 1][self.y] != -1:
            self.neighbors.append(Node(
                self.x - 1, self.y, self.cost + grid[self.x - 1][self.y], self.depth + 1, self, "U"))

        # RIGHT DIAGONAL UP - RU
        if self.x > 0 and self.y < size - 1 and (grid[self.x - 1][self.y] != -1 and grid[self.x][self.y + 1] != -1) and grid[self.x - 1][self.y + 1] != -1:
            self.neighbors.append(Node(
                self.x - 1, self.y + 1, self.cost + grid[self.x - 1][self.y + 1], self.depth + 1, self, "RU"))

        # return the neighbors list
        self.neighbors.reverse()
        return self.neighbors

    """
    The function returns the path from the start point to the end point
    """

    def solution(self):
        path = []
        px, py = self.parent.get_pos()
        tmp_node = self
        while px != tmp_node.x or py != tmp_node.y:
            path.append(tmp_node.direction)
            tmp_node = tmp_node.parent
            px, py = tmp_node.get_parent().get_pos()
        return path

    """
    The function compare between two nodes in order to check if they equals
    """

    def compare(self, node):
        return self.get_pos() == node.get_pos()
