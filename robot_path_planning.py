# ---------------------------------------------------------
# ROBOT PATH PLANNING USING A* ALGORITHM (Worksheet 7)
# ---------------------------------------------------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import heapq


def heuristic(a, b):
    """Manhattan distance"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_neighbors(node, rows, cols):
    """Get valid 4-directional neighbor nodes"""
    r, c = node
    for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            yield (nr, nc)


def a_star(grid, start, end):
    """A* algorithm"""
    rows, cols = grid.shape
    pq = []
    heapq.heappush(pq, (0, start))

    came_from = {start: None}
    g = {start: 0}

    while pq:
        _, current = heapq.heappop(pq)

        if current == end:
            # Rebuild path
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        for n in get_neighbors(current, rows, cols):
            if grid[n] == 1:  # obstacle
                continue

            new_g = g[current] + 1

            if n not in g or new_g < g[n]:
                g[n] = new_g
                f = new_g + heuristic(n, end)
                heapq.heappush(pq, (f, n))
                came_from[n] = current

    return None  # no path


def main():
    # User inputs
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    grid = np.zeros((rows, cols), dtype=int)

    obs_count = int(input("Enter number of obstacles: "))
    for _ in range(obs_count):
        r = int(input("Obstacle row: "))
        c = int(input("Obstacle col: "))
        grid[r][c] = 1

    start = tuple(map(int, input("Enter start (row col): ").split()))
    end = tuple(map(int, input("Enter end (row col): ").split()))

    print("\nGRID BEFORE PATHFINDING:")
    print(pd.DataFrame(grid))

    # Run A*
    path = a_star(grid, start, end)

    if path is None:
        print("NO VALID PATH FOUND!")
        return

    print("\nShortest Path Found:")
    print(path)

    # Visualization
    plt.imshow(grid, cmap="gray_r")

    # path (red dots)
    for r, c in path:
        plt.plot(c, r, "ro")

    # start (green)
    plt.plot(start[1], start[0], "go", markersize=10)

    # end (blue)
    plt.plot(end[1], end[0], "bo", markersize=10)

    plt.title("A* Robot Path Planning")
    plt.show()



main()
