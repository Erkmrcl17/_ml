import numpy as np
from random import randint, shuffle

citys = [
    (0, 3), (0, 0), (0, 2), (0, 1),
    (1, 0), (1, 3), (2, 0), (2, 3),
    (3, 0), (3, 3), (3, 1), (3, 2)
]

def distance(a, b):
    return ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5

def pathLength(path):
    return sum(distance(path[i], path[(i + 1) % len(path)]) for i in range(len(path)))

def neighbor(route):
    new_route = route[:]
    idx1, idx2 = randint(0, len(route) - 1), randint(0, len(route) - 1)
    new_route[idx1], new_route[idx2] = new_route[idx2], new_route[idx1]
    return new_route

def hillClimbing(x, pathLength, neighbor, max_fail):
    print("start: ", pathLength(x))
    fail = 0
    gens = 0
    while True:
        nx = neighbor(x)
        if pathLength(nx) < pathLength(x):
            x = nx
            gens += 1
            print(gens,  ':', pathLength(x), x)
            fail = 0
        else:
            fail += 1
            if fail > max_fail:
                print("solution: ", pathLength(x))
                return x

hillClimbing(citys, pathLength, neighbor, max_fail=10000)