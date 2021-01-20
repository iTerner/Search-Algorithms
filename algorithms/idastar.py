from node import Node
from algorithms.heuristicfunction import h
import math

"""
The f cost function for the IDA* algorithm
"""


def f(node, goal):
    # compute the h and g score
    h_score = h(node.get_pos(), goal)
    g_score = node.get_cost()
    return h_score + g_score


"""
The function who compute the best path for the IDA* algorithm
"""


def DFS_contour(node, f, f_limit, problem):
    tmp = f(node, problem.get_end())
    if tmp > f_limit:
        return None, tmp
    # check if we get to the end node
    if problem.is_goal(node):
        return node.solution(), f_limit
    next_f = math.inf
    for n in node.update_neighbors(problem):
        sol, new_f = DFS_contour(n, f, f_limit, problem)
        if sol:
            return sol, new_f
        next_f = min(next_f, new_f)
    return None, next_f


"""
implemention of the IDA* algorithm
"""


def IDAStar(problem):
    x, y = problem.get_start()
    grid = problem.get_grid()
    start_node = Node(x, y, grid[x][y], 0, Node(x, y, 0, 0, None, ""), "")
    f_limit = f(start_node, problem.get_end())
    while True:
        sol, f_limit = DFS_contour(start_node, f, f_limit, problem)
        if sol:
            return sol
        if f_limit == math.inf:
            return "no path"
