import math
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from typing import List
from matplotlib.patches import Polygon


def random_point_in_triangle(vertices: List[np.ndarray]):
    if len(vertices) != 3:
        raise ValueError("Invalid number of vertices")

    u, v = np.random.rand(2)
    if u + v > 1:
        u, v = 1 - u, 1 - v

    return (1 - u - v) * vertices[0] + u * vertices[1] + v * vertices[2]


side_length = 100
N = 100000
interval = 0.005  # ms

height = math.sin(math.pi / 3) * side_length
# vertices
a1 = np.array([0, 0])
a2 = np.array([side_length, 0])
a3 = np.array([side_length / 2, height])
triangle_vertices = [a1, a2, a3]

triangle = Polygon(triangle_vertices, closed=True, edgecolor="black", facecolor="white")

fig, ax = plt.subplots()
ax.add_patch(triangle)

X = []
Y = []

start = random_point_in_triangle(triangle_vertices)
X.append(start[0])
Y.append(start[1])
for i in range(N):
    vertex = random.choice(triangle_vertices)
    X.append((vertex[0] + X[-1]) / 2)
    Y.append((vertex[1] + Y[-1]) / 2)

sc = ax.scatter([], [], s=0.5)
ax.set_xlim(-1, a2[0] + 1)
ax.set_ylim(-1, a3[1] + 1)
ax.set_aspect("equal")


def update(frame):
    x = X[:frame]
    y = Y[:frame]
    sc.set_offsets(np.column_stack((x, y)))
    return (sc,)


ani = animation.FuncAnimation(
    fig, update, frames=N + 1, interval=interval, blit=True, repeat=False
)

plt.show()
