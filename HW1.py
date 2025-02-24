import random

def hillClimbing(x, height, neighbor, max_fail=10000):
    fail = 0
    while True:
        nx = neighbor(x)
        if height(nx)>height(x):
            x = nx
            fail = 0
        else:
            fail += 1
            if fail > max_fail:
                return x

def neighbor(x, nx=0.01):
    return [coordinate + random.uniform(-nx, nx) for coordinate in x]

def evaluate_height(point):
    x, y, z = point
    return -(x**2 + y**2 + z**2 - 2*x - 4*y - 6*z + 8)


initial_point = [0, 0, 0]
best_point = hillClimbing(initial_point, evaluate_height, neighbor)
print(best_point)
