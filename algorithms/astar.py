from algorithms.bfgs import BFGS
from algorithms.heuristicfunction import h

"""
The implementation of the A* path finder algorithm
"""


def AStar(problem):
    """
    The cost funciton for the A* algorithm
    """
    def g(node):
        h_score = h(node.get_pos(), problem.get_end())
        g_score = float(node.get_cost())
        return (g_score + h_score)
    res = BFGS(problem, f=g)
    return res
