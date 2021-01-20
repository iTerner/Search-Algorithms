"""
The heuristic function using in the A* algorithm
"""


def h(current, goal):
    x1, y1 = current
    x2, y2 = goal
    return abs(x1 - x2) + abs(y1 - y2)
