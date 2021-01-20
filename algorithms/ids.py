from node import Node

"""
The funtion runs the Depth First Search algorithm on a given problem
"""


def DFS_L(problem):
    x, y = problem.get_start()
    grid = problem.get_grid()
    limit = problem.get_limit()
    frontier = [Node(x, y, grid[x][y], 0, Node(x, y, 0, 0, None, ""), "")]
    while frontier:
        node = frontier.pop()
        if problem.is_goal(node):
            return node.solution()
        if node.get_depth() < limit:
            neighbors = node.update_neighbors(problem)
            for n in neighbors:
                frontier.append(n)
    return None


"""
The Iterative Depth Search algorithm
"""


def IDS(problem):
    for limit in range(2, 20):
        # set the new limit for the problem
        problem.set_limit(limit)
        # check if we find a solution
        res = DFS_L(problem)
        if res:
            return res

    return "no path"
