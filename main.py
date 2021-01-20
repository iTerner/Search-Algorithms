from algorithms.ids import IDS
from problem import Problem
from algorithms.ucs import UCS
from algorithms.astar import AStar
from algorithms.idastar import IDAStar

"""
The function get from the user:
The algorithm name: IDS, UCS, A-STAR or IDA-STAR
The start and end point
The size of the grid and the cost for each node

The function returns the data
"""


def get_data():
    algo_name = input()
    start_point = input()
    end_point = input()
    grid_size = int(input())
    grid = []
    for i in range(grid_size):
        grid.append(list(map(int, input().split(","))))
    start_point = tuple(int(num) for num in start_point.replace(',', ''))
    end_point = tuple(int(num) for num in end_point.replace(',', ''))
    return algo_name, start_point, end_point, grid_size, grid


"""
The function gets an algorithm name and a search problem.
The funtion runs the algorithm on the search problem and prints the path and the 
length of the path if there is a path between the start pont and the end point. otherwise the function 
prints "no path"
"""


def run(algo_name, p):
    res = 0
    if algo_name == "IDS":
        res = IDS(p)
    elif algo_name == "UCS":
        res = UCS(p)
    elif algo_name == "ASTAR":
        res = AStar(p)
    elif algo_name == "IDASTAR":
        res = IDAStar(p)

    if type(res) == list:
        print(len(res))
        tmp = res.reverse()
    print(res)


def main():
    # get the data from the user
    algo_name, start_point, end_point, grid_size, grid = get_data()
    p = Problem(start_point, end_point, 0, grid, grid_size)
    # run the search algorithm on the problem p
    run(algo_name, p)


main()
