# main.py
import ctypes
from ctypes import Structure, c_double, c_int
import matplotlib.pyplot as plt

class Point(Structure):
    _fields_ = [("x", c_double), ("y", c_double)]

class SolutionSet(Structure):
    _fields_ = [("sols", Point * 2), ("count", c_int)]

# Load C lib
lib = ctypes.CDLL("./libsolver.so")
lib.solve_equations.restype = SolutionSet

# Call function
solutions = lib.solve_equations()
print(f"Found {solutions.count} solutions:")
for i in range(solutions.count):
    x, y = solutions.sols[i].x, solutions.sols[i].y
    print(f"Solution {i+1}: ({x}, {y})")

# Plot equations and solutions
import numpy as np
x_vals = np.linspace(-1, 3, 400)
y1 = (6*x_vals)/(6*x_vals - 3)   # from eqn (1)
y2 = (2*x_vals)/(5*x_vals - 4)   # from eqn (2)

plt.figure(figsize=(6,6))
plt.plot(x_vals, y1, label="6x+3y=6xy")
plt.plot(x_vals, y2, label="2x+4y=5xy")
for i in range(solutions.count):
    x, y = solutions.sols[i].x, solutions.sols[i].y
    plt.scatter(x, y, c='r', zorder=5)
    plt.text(x, y, f"({x:.0f},{y:.0f})", fontsize=10)

plt.ylim(-1,4)
plt.grid(True)
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Solutions of nonlinear system")
plt.show()

