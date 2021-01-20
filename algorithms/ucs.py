from algorithms.bfgs import BFGS


"""
Uniform Cost Search algorithm
"""


def UCS(problem):
    """
    The cost function for the Uniform Cost Search algorithm.
    The function returns the cost of the node
    """
    def g(node):
        return float(node.get_cost())
    res = BFGS(problem, f=g)
    return res
