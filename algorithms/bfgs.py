from node import Node

"""
The function get the node in the frontier.
we assume that there is a node with the same position in the frontier because the
node was in the frontier.
The function returns the node with the same position from the frontier.
"""


def get_node_from_frontier(frontier, node):
    for e in frontier:
        if node.compare(e):
            return e
    return None


"""
The function return the index of the node in the frontier.
"""


def get_node_index(frontier, node):
    count = 0
    for e in frontier:
        if node.compare(e):
            return count
        count += 1
    return None


"""
The function returns True if the node is in the closed set and
False otherwie
"""


def is_node_in_closed_list(l, node):
    for e in l:
        if node.compare(e):
            return True
    return False


"""
Best First Graph Search algorithm.
The funtion runs the Best First Graph Search algorithm on a given search problem with
a cost function f.
"""


def BFGS(problem, f):
    x, y = problem.get_start()
    grid = problem.get_grid()
    # create the frontier
    frontier = []
    frontier.append(
        (0, Node(x, y, grid[x][y], 0, Node(x, y, 0, 0, None, ""), "")))
    # create the closed set
    closed_list = set()
    count = 0
    while frontier:
        frontier = sorted(frontier, key=lambda x: x[0])
        node = frontier.pop(0)[1]
        count += 1
        if problem.is_goal(node):
            # print(count)
            return node.solution()
        closed_list.add(node)
        children = node.update_neighbors(problem)
        for child in children:
            if not is_node_in_closed_list(closed_list, child) and child not in frontier:
                frontier.append((f(child), child))
            elif child in frontier and f(child) < f(get_node_from_frontier(frontier, child)):
                index = get_node_index(
                    frontier, get_node_from_frontier(frontier, child))
                del frontier[index]
                frontier.append((f(child), child))
    return None
